def find_rbac_smells(role_assignments: list, subscription_id: str) -> list:
    """
    Inspect RBAC role assignments and return a list of RBAC-related smells.
    """
    smells = []

    sub_scope = f"/subscriptions/{subscription_id}"

    for ra in role_assignments:
        scope = ra.get("scope", "")
        role = ra.get("roleDefinitionName", "")
        principal = ra.get("principalName", "")
        ptype = ra.get("principalType", "")

        # Smell 1: Owner at subscription scope
        if role == "Owner" and scope == sub_scope:
            smells.append({
                "signal": "rbac_owner_on_subscription",
                "scope": scope,
                "role": role,
                "principalType": ptype,
                "principalName": principal,
                "detail": "High privilege role assigned at subscription scope"
            })

        # Smell 2: Contributor on legacy RG
        if role == "Contributor" and "/resourceGroups/rg-legacy-misc" in scope:
            smells.append({
                "signal": "rbac_contributor_on_legacy_rg",
                "scope": scope,
                "role": role,
                "principalType": ptype,
                "principalName": principal,
                "detail": "Contributor role on legacy/misc resource group"
            })

    return smells