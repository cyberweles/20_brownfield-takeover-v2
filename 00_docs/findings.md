# Findings (v0)

This document summarizes the key findings identified during the initial brownfield assessment.
Findings are based on snapshot data and hygiene metrics. No remediation has been applied yet.

---

## BF-001 — Storage account allows legacy TLS

**Resource:** `stprodcoredat01` (rg-prod-core)  
**Signal:** `storage_legacy_tls`  

**Impact:**  
Legacy TLS versions increase the risk of weak cryptography and may violate security baselines and compliance requirements.

**Evidence:**  
- `minimumTlsVersion=TLS1_0` detected in snapshot.

**Suggested action (non-destructive):**  
- Update minimum TLS version to TLS1_2 via IaC.
- Validate client compatibility before enforcement.

---

## BF-002 — Public blob access enabled on storage account

**Resource:** `stprodcoredat01` (rg-prod-core)  
**Signal:** `storage_blob_public_access`

**Impact:**  
Public blob access may lead to unintended data exposure.

**Evidence:**  
- `allowBlobPublicAccess=true` detected.

**Suggested action:**  
- Disable public blob access.
- Validate if any workloads rely on anonymous access.

---

## BF-003 — Key Vault accessible from public network

**Resource:** `kv-prod-apps` (rg-prod-apps)  
**Signal:** `keyvault_public_network_access`

**Impact:**  
Public network access increases attack surface for sensitive secrets and keys.

**Evidence:**  
- `publicNetworkAccess=Enabled`.

**Suggested action:**  
- Restrict access to private endpoints or trusted networks.
- Introduce baseline policy in audit mode first.

---

## BF-004 — Public IP present in production core resources

**Resource:** `pip-prod-legacy` (rg-prod-core)  
**Signal:** `public_ip_present`

**Impact:**  
Public IPs may expose internal services and should be explicitly justified.

**Evidence:**  
- Public IP resource exists in production RG.

**Suggested action:**  
- Confirm business need.
- Consider replacement with private connectivity.

---

## BF-005 — Owner role assigned at subscription scope

**Principal:** `founder@company.invalid`  
**Signal:** `rbac_owner_on_subscription`

**Impact:**  
Broad privileges at subscription scope increase blast radius in case of credential compromise.

**Evidence:**  
- `Owner` role assigned at subscription scope.

**Suggested action:**  
- Reduce to least-privilege role.
- Introduce break-glass process if required.

---

## BF-006 — Contributor role on legacy resource group

**Principal:** `ex-employee@company.invalid`  
**Signal:** `rbac_contributor_on_legacy_rg`

**Impact:**  
Stale access increases security risk and audit complexity.

**Evidence:**  
- Contributor role assigned on `rg-legacy-misc`.

**Suggested action:**  
- Review access necessity.
- Remove or downgrade role assignment.

---
