# Brownfield snapshot (synthetic)

This folder contains a **reconstructed** (“synthetic”) snapshot of an organically grown Azure environment.
It is used to practice **assessment and decision-making** (inventory → hygiene metrics → findings → plan),
not to fake scale.

## Files
- `subscription.json` – subscription context (simulated `az account show`)
- `resourcegroups.json` – resource group inventory + tags (simulated `az group list`)
- `resources.json` – resource inventory + selected properties (simulated `az resource list --expand properties`)
- `role_assignments.json` – RBAC assignments for IAM hygiene (simulated `az role assignment list --all`)
- `policy_state.json` – policy assignments (audit-mode example)
- `diagnostics_state.json` – simplified diagnostics coverage signals (tracked scopes)

## Notes
- No secrets are stored here.
- The dataset intentionally includes typical brownfield issues:
  - missing/partial tags (owner/costCenter/env)
  - public exposure signals (public IP, public network access)
  - legacy TLS and public blob access on storage
  - over-privileged/stale RBAC assignments
