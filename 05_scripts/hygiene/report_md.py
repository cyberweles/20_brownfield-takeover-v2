from pathlib import Path


def write_report_md(out_path: Path, meta: dict, metrics: dict, lists: dict):
    """
    Write a minimal Markdown report (v0):
    - META
    - TAG COVERAGE
    - EXPOSURE SIGNALS
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# Hygiene Report (v0)")
    lines.append("")
    lines.append("## Meta")
    lines.append(f"- Generated (UTC): `{meta['generated_utc']}`")
    lines.append(f"- Subscription: `{meta['subscription_name']}` (`{meta['subscription_id']}`)")
    lines.append("")
    lines.append("## Tag coverage (required: owner, costCenter, env)")
    lines.append(f"- Resource Groups: **{metrics['rg_tag_ok']}/{metrics['rg_total']} ({metrics['rg_tag_ok_pct']}%)**")
    lines.append(f"- Resources: **{metrics['res_tag_ok']}/{metrics['res_total']} ({metrics['res_tag_ok_pct']}%)**")
    lines.append("")

    # ---- Exposure section ----
    lines.append("## Exposure signals")
    exposure = lists.get("exposure", [])
    if exposure:
        for s in exposure:
            lines.append(
                f"- `{s['signal']}` — `{s['resource_group']}` / `{s['resource_name']}` — {s['detail']}"
            )
    else:
        lines.append("- None")
    lines.append("")

    # ---- RBAC section ----
    lines.append("## RBAC smells")
    rbac = lists.get("rbac", [])
    if rbac:
        for s in rbac:
            lines.append(
                f"- `{s['signal']}` — `{s['role']}` at `{s['scope']}` — "
                f"`{s['principalName']}` ({s['principalType']})"
            )
    else:
        lines.append("- None")
    lines.append("")

    out_path.write_text("\n".join(lines), encoding="utf-8")