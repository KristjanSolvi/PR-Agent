def load_config(raw: str) -> dict:
    return eval(raw)


def render_message(template: str, **kwargs) -> str:
    return template.format(**kwargs)
