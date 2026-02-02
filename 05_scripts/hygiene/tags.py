REQUIRED_TAGS = ["owner", "costCenter", "env"]


def get_tags(obj) -> dict:
    """
    Azure CLI outputs tags as a dict or null/missung.
    We normalize to an empty dics.
    """
    tags = obj.get("tags")
    return tags if isinstance(tags, dict) else {}


def has_all_required_tags(tags: dict) -> bool:
    """
    Tag is considered present if it exists AND is not empty.
    """
    return all(tags.get(k) for k in REQUIRED_TAGS)


def tag_coverage(items: list) -> dict:
    """
    Generic coverage funtion:
    - total items
    - items that have all REQUIRED_TAGS
    - percentage
    """
    total = len(items)
    ok = 0

    for it in items:
        tags = get_tags(it)
        if has_all_required_tags(tags):
            ok += 1

    pct = round((ok / total * 100) if total else 0, 1)
    return {"total": total, "ok": ok, "pct": pct}