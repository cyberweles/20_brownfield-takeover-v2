from pathlib import Path


def plot_coverage(out_png: Path, metrics: dict) -> bool:
    """
    Create a simple bar chart from coverage metrics.
    Returns True if chart created, False if matplotlib missing.
    """
    try:
        import matplotlib.pyplot as plt
    except Exception:
        return False
    
    labels = ["RG tags", "Res tags"]
    values = [metrics["rg_tag_ok_pct"], metrics["res_tag_ok_pct"]]

    out_png.parent.mkdir(parents=True, exist_ok=True)

    plt.figure()
    plt.bar(labels, values)
    plt.ylim(0, 100)
    plt.ylabel("Coverage (%)")
    plt.title("Brownfield hygiene coverage (v0)")
    plt.tight_layout()
    plt.savefig(out_png)
    plt.close()
    return True