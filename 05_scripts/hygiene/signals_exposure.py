def tls_is_legacy(value: str) -> bool:
    # Azure storage values like: TLS1_0, TLS1_1, TLS1_2
    return value in ("TLS1_0", "TLS1_1")


def find_exposure_signals(resources: list) -> list:
    """
    Inspect resources and return a list of exposure-related signals.
    Each signal is a dict (easy to render later).
    """
    signals = []

    for r in resources:
        rid = r.get("id", "")
        rtype = r.get("type", "")
        rg = r.get("resourceGroup", "")
        name = r.get("name", "")
        props = r.get("properties", {}) or {}

        # Public IP resource existence (simple signal)
        if rtype == "Microsoft.Network/publicIPAddresses":
            signals.append({
                "signal": "public_ip_present",
                "resource_id": rid,
                "resource_type": rtype,
                "resource_group": rg,
                "resource_name": name,
                "detail": "Public IP resource exists"
            })

        # Storage checks
        if rtype == "Microsoft.Storage/storageAccounts":
            min_tls = props.get("minimumTlsVersion")
            allow_public_blob = props.get("allowBlobPublicAccess")
            pna = props.get("publicNetworkAccess")

            if tls_is_legacy(min_tls):
                signals.append({
                    "signal": "storage_legacy_tls",
                    "resource_id": rid,
                    "resource_type": rtype,
                    "resource_group": rg,
                    "resource_name": name,
                    "detail": f"minimumTlsVersion={min_tls}"
                })

            if allow_public_blob is True:
                signals.append({
                    "signal": "storage_blob_public_access",
                    "resource_id": rid,
                    "resource_type": rtype,
                    "resource_group": rg,
                    "resource_name": name,
                    "detail": "allowBlobPublicAccess=true"
                })

            if pna == "Enabled":
                signals.append({
                    "signal": "storage_public_network_access",
                    "resource_id": rid,
                    "resource_type": rtype,
                    "resource_group": rg,
                    "resource_name": name,
                    "detail": "publicNetworkAccess=Enabled"
                })

            # Key Vault checks
            if rtype == "Microsoft.KeyVault/vaults":
                pna = props.get("publicNetworkAccess")
                if pna == "Enabled":
                    signals.append({
                        "signal": "keyvault_public_network_access",
                        "resource_id": rid,
                        "resource_type": rtype,
                        "resource_group": rg,
                        "resource_name": name,
                        "detail": "publicNetworkAccess=Enabled"
                    })

    return signals