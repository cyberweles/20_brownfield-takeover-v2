import csv
from pathlib import Path


def write_metrics_csv(out_path: Path, metrics: dict):
    """
    Write a simple 'metric,value' CSV.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["metric", "value"])
        for key, value in metrics.items():
            w.writerow([key, value])