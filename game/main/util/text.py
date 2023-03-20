__ESCAPE_MAPPING: dict[str, str] = ...


def escape(content: str) -> str:
    return (
        content.replace("{", "(").replace("}", ")").replace("[", "(").replace("]", ")")
    )
