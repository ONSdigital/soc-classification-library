"""SOC metadata helpers for lookup enrichment.

This module provides an in-code SOC metadata model, mirroring SIC's
in-library metadata approach and avoiding Excel/config startup dependency.
"""

SOC_META: dict[str, dict[str, object]] = {
    "1": {
        "group_title": "Managers directors and senior officials",
        "group_description": (
            "Occupations focused on planning directing and coordinating "
            "organisational resources."
        ),
        "entry_routes_and_quals": "",
        "tasks": [],
    },
    "2": {
        "group_title": "Professional occupations",
        "group_description": (
            "Occupations requiring high levels of specialist knowledge and "
            "professional expertise."
        ),
        "entry_routes_and_quals": "",
        "tasks": [],
    },
    "3": {
        "group_title": "Associate professional and technical occupations",
        "group_description": (
            "Occupations supporting professional services with technical and "
            "practical expertise."
        ),
        "entry_routes_and_quals": "",
        "tasks": [],
    },
    "4": {
        "group_title": "Administrative and secretarial occupations",
        "group_description": (
            "Occupations focused on administration record keeping and office support."
        ),
        "entry_routes_and_quals": "",
        "tasks": [],
    },
    "5": {
        "group_title": "Skilled trades occupations",
        "group_description": "",
        "entry_routes_and_quals": "",
        "tasks": [],
    },
    "6": {
        "group_title": "Caring leisure and other service occupations",
        "group_description": "",
        "entry_routes_and_quals": "",
        "tasks": [],
    },
    "7": {
        "group_title": "Sales and customer service occupations",
        "group_description": "",
        "entry_routes_and_quals": "",
        "tasks": [],
    },
    "8": {
        "group_title": "Process plant and machine operatives",
        "group_description": "",
        "entry_routes_and_quals": "",
        "tasks": [],
    },
    "9": {
        "group_title": "Elementary occupations",
        "group_description": "",
        "entry_routes_and_quals": "",
        "tasks": [],
    },
    "1111": {
        "group_title": "Chief executives and senior officials",
        "group_description": (
            "Chief executives and senior officials head large enterprises "
            "and organisations."
        ),
        "entry_routes_and_quals": "Entry is typically through significant leadership experience.",
        "tasks": ["Define organisational strategy", "Lead senior teams"],
    },
    "2112": {
        "group_title": "Biological scientists",
        "group_description": (
            "Biological scientists research living organisms and " "biological systems."
        ),
        "entry_routes_and_quals": "Usually requires a relevant scientific degree.",
        "tasks": ["Design and conduct research", "Analyse biological data"],
    },
    "2314": {
        "group_title": "Primary education teaching professionals",
        "group_description": (
            "Primary education teaching professionals teach children in "
            "primary schools."
        ),
        "entry_routes_and_quals": "Qualified teacher status is typically required.",
        "tasks": ["Plan lessons", "Deliver classroom teaching"],
    },
    "4111": {
        "group_title": "National government administrative occupations",
        "group_description": (
            "Administrative occupations delivering national government "
            "services and processes."
        ),
        "entry_routes_and_quals": "Entry routes vary by department and role.",
        "tasks": ["Maintain records", "Support case administration"],
    },
}


class SocMeta:  # pylint: disable=too-few-public-methods
    """In-code SOC metadata lookup."""

    def __init__(self):
        self.soc_meta = SOC_META

    def get_meta_by_code(self, code: str, allow_parent_fallback: bool = True) -> dict:
        """Retrieve title and details for a given SOC code.

        Args:
            code: SOC code to resolve.
            allow_parent_fallback: If True, progressively trims trailing
                digits until a parent-group entry is found.
        """
        entry = self.soc_meta.get(code)
        if entry is not None:
            return {
                "code": code,
                "group_title": entry.get("group_title", ""),
                "group_description": entry.get("group_description", ""),
                "entry_routes_and_quals": entry.get("entry_routes_and_quals", ""),
                "tasks": entry.get("tasks", []),
            }

        if allow_parent_fallback:
            lookup = code[:-1]
            while lookup:
                entry = self.soc_meta.get(lookup)
                if entry is not None:
                    return {
                        "code": lookup,
                        "group_title": entry.get("group_title", ""),
                        "group_description": entry.get("group_description", ""),
                        "entry_routes_and_quals": entry.get(
                            "entry_routes_and_quals", ""
                        ),
                        "tasks": entry.get("tasks", []),
                    }
                lookup = lookup[:-1]
        return {"error": f"No metadata found for SOC code {code}"}
