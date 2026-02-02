## Prioritized remediation plan (v0)

1. **Security baseline first**
   - Address legacy TLS and public access on storage accounts.
   - Review Key Vault network exposure.

2. **Access hygiene**
   - Reduce Owner privileges at subscription level.
   - Clean up stale RBAC assignments.

3. **Governance guardrails**
   - Enforce required tags via policy (audit → enforce).
   - Introduce diagnostic settings baseline.

4. **Convergence to IaC**
   - Import selected resources into Terraform.
   - Apply changes incrementally and non-destructively.

All actions are planned as incremental steps with verification after each change.
