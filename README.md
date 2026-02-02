# 20_brownfield-takeover-v2

Brownfield Azure platform takeover (v2): **snapshot-based assessment → findings → plan → non-destructive convergence to Terraform**, with lightweight hygiene reporting (tags/diagnostics/public exposure).

## What this is
- A realistic **platform-engineering case study** based on:
  - exported ARM snapshots (JSON)
  - a minimal Terraform intent (import/converge, non-destructive)
  - a small hygiene report generated from data (CSV/MD + optional chart)

## What this is NOT
- Not an enterprise lading zone framework
- Not a full remediation engine
- No auto-fix — changes are explicit and reviewed

## Repo structure
- `00_docs/` — context, scope, findings, plan, decisions
- `01_iac/` — Terraform (convergence to IaC)
- `02_ops/` — export + verify scripts
- `03_data/brownfield_snapshot/` — "existing" state snapshots (JSON)
- `04_reports/` — generated reports (md/csv/png)
- `05_scripts/` — small tools (Python)

## Quick start (local)
1. Put snapshot JSON files into `03_data/brownfield_snapshot/`
2. Run export / verify scripts from `02_ops/`
3. Generate a hygiene report from snapshot data

## Assessment Pack (v0)

This repo contains a reconstructured brownfield snapshot and a small hygiene report generator.

### Generate report (WSL)
```bash
python3 -m 05_scripts.hygiene.main
```

Outputs:
- `04_reports/hygiene.csv` (metrics)
- `04_reports/report.md` (human-readable report)

### Optional chart

Chart generation requires matplotlib:
```bash
python3 -m venv .venv
source .venv/bin/acctivate
python -m pip install -U pip
python -m pip install matplotlib
python -m 05_scripts.hygiene.main --plot
```

Outputs:
- `04_reports/hygiene.png`

**Note:** Snapshot data is intentionally reconstructed to simulate a 2-3 year organically grown Azure environment. The goal is to practice assessment and decision-making, not to fake scale.