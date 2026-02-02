# Hygiene Report (v0)

## Meta
- Generated (UTC): `2026-02-02T18:06:04+00:00`
- Subscription: `sub-brownfield-v2-simulated` (`00000000-0000-0000-0000-000000000000`)

## Tag coverage (required: owner, costCenter, env)
- Resource Groups: **2/5 (40.0%)**
- Resources: **3/8 (37.5%)**

## Exposure signals
- `public_ip_present` — `rg-prod-core` / `pip-prod-legacy` — Public IP resource exists
- `storage_legacy_tls` — `rg-prod-core` / `stprodcoredat01` — minimumTlsVersion=TLS1_0
- `storage_blob_public_access` — `rg-prod-core` / `stprodcoredat01` — allowBlobPublicAccess=true
- `storage_public_network_access` — `rg-prod-core` / `stprodcoredat01` — publicNetworkAccess=Enabled
- `storage_public_network_access` — `rg-dev-sbx` / `stdevscratch01` — publicNetworkAccess=Enabled

## RBAC smells
- `rbac_owner_on_subscription` — `Owner` at `/subscriptions/00000000-0000-0000-0000-000000000000` — `founder@company.invalid` (User)
- `rbac_contributor_on_legacy_rg` — `Contributor` at `/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg-legacy-misc` — `ex-employee@company.invalid` (User)
