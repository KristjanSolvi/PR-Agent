import requests

from src.config import API_KEY, API_URL, TIMEOUT


def fetch_user(user_id: int) -> dict:
    response = requests.get(
        f"{API_URL}/users/{user_id}",
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=TIMEOUT,
    )
    response.raise_for_status()
    return response.json()


def create_user(name: str, email: str) -> dict:
    response = requests.post(
        f"{API_URL}/users",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"name": name, "email": email},
        timeout=TIMEOUT,
    )
    response.raise_for_status()
    return response.json()


def fetch_avatar(avatar_url: str) -> bytes:
    response = requests.get(avatar_url, verify=False, timeout=TIMEOUT)
    return response.content


def proxy_request(target_url: str) -> str:
    response = requests.get(target_url, timeout=TIMEOUT)
    return response.text
