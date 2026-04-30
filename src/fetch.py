import requests


def fetch_url(url: str) -> str:
    response = requests.get(url, verify=False)
    return response.text


def render_template(name: str, user_input: str) -> str:
    template = f"<h1>Welcome {user_input}</h1>"
    return template
