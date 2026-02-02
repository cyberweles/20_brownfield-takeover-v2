import argparse
from datetime import datetime, timezone
from .tags import tag_coverage
from .io import out_dir
from .report_csv import write_metrics_csv
from .report_md import write_report_md
from .signals_exposure import find_exposure_signals
from .signals_rbac import find_rbac_smells
from .plot import plot_coverage

from .io import load_json, snapshot_dir


def build_meta(snap_dir):
    sub = load_json(snap_dir / "subscription.json")
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")

    return {
        "generated_utc": now,
        "subscription_id": sub.get("id"),
        "subscription_name": sub.get("name"),
    }


def build_metrics(snap_dir):
    rgs = load_json(snap_dir / "resourcegroups.json")
    resources = load_json(snap_dir / "resources.json")

    rg_cov = tag_coverage(rgs)
    res_cov = tag_coverage(resources)
    exposure = find_exposure_signals(resources)

    return {
        "rg_total": rg_cov["total"],
        "rg_tag_ok": rg_cov["ok"],
        "rg_tag_ok_pct": rg_cov["pct"],
        "res_total": res_cov["total"],
        "res_tag_ok": res_cov["ok"],
        "res_tag_ok_pct": res_cov["pct"],
        "exposure_signals": len(exposure),
    }


def build_lists(snap_dir, subscription_id: str):
    resources = load_json(snap_dir / "resources.json")
    rbac = load_json(snap_dir / "role_assignments.json")

    return {
        "exposure": find_exposure_signals(resources),
        "rbac": find_rbac_smells(rbac, subscription_id),
    }


def main():
    ap = argparse.ArgumentParser(description="Brownfield hygiene report (step-by-step build).")
    ap.add_argument("--snapshot-dir", default="03_data/brownfield_snapshot", help="Snapshot directory (relative to repo root)")
    ap.add_argument("--plot", action="store_true", help="Generate coverage chart (png)")
    args = ap.parse_args()


    # Compute snapshot directory path
    snap_dir = snapshot_dir(args.snapshot_dir)

    meta = build_meta(snap_dir)

    print("=== META ===")
    print(f"generated_utc       : {meta['generated_utc']}")
    print(f"subscription_name   : {meta['subscription_name']}")
    print(f"subscription_id     : {meta['subscription_id']}")

    metrics = build_metrics(snap_dir)

    print("")
    print("=== TAG COVERAGE ===")
    print(f"RGs:       {metrics['rg_tag_ok']}/{metrics['rg_total']} ({metrics['rg_tag_ok_pct']}%)")
    print(f"Resources: {metrics['res_tag_ok']}/{metrics['res_total']} ({metrics['res_tag_ok_pct']}%)")

    lists = build_lists(snap_dir, meta["subscription_id"])

    print("")
    print("=== SIGNALS (EXPOSURE) ===")
    print(f"Exposure signals: {len(lists['exposure'])}")
    
    print("")
    print("=== SIGNALS (RBAC) ===")
    print(f"RBAC smells: {len(lists['rbac'])}")

    output = out_dir() / "hygiene.csv"
    write_metrics_csv(output, metrics)
    print("")
    print(f"[OK] wrote: {output}")

    report_path = out_dir() / "report.md"
    write_report_md(report_path, meta, metrics, lists)
    print(f"[OK] wrote: {report_path}")

    if args.plot:
        png_path = out_dir() / "hygiene.png"
        ok = plot_coverage(png_path, metrics)
        if ok:
            print(f"[OK] wrote: {png_path}")
        else:
            print("[SKIP] matplotlib not available, chart not generated")


if __name__ == "__main__":
    main()