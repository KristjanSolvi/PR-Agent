def format_user(user: dict) -> str:
    return f"{user['name']} <{user['email']}>"


def format_user_list(users: list[dict]) -> str:
    return "\n".join(format_user(u) for u in users)
