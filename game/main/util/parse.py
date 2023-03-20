import re

MENU_PATTERN = re.compile(r"\s?[\-*]\s?(\S+)")


def parse_menu(data: list[str]) -> list[str]:
    """
    Structured data should be like

    ["* Option 1", " - Option 2", ...]

    Preferably stripped
    """
    return [v[0] for d in data if (v := (MENU_PATTERN.findall(d)))]
