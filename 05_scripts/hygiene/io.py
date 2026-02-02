import json
from pathlib import Path


def load_json(path: Path):
    """Load JSON from a file and return Python object (dict/list)."""
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)
    

def get_repo_root() -> Path:
    """
    Return repo root based on this file location"
    .../05_scripts/hygiene/io.py -> repo root is 2 parents up from '05_scripts'.
    """
    return Path(__file__).resolve().parents[2]


def snapshot_dir(default_rel: str = "03_data/brownfield_snapshot") -> Path:
    """Return absolute path to snapshot directory."""
    return (get_repo_root() / default_rel).resolve()


def out_dir(default_rel: str = "04_reports") -> Path:
    """Return absolute path to output directory."""
    return (get_repo_root() / default_rel).resolve()