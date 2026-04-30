from src.utils.formatter import format_user, format_user_list


def test_format_user():
    user = {"name": "Alice", "email": "alice@example.com"}
    assert format_user(user) == "Alice <alice@example.com>"


def test_format_user_list():
    users = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
    ]
    result = format_user_list(users)
    assert "Alice <alice@example.com>" in result
    assert "Bob <bob@example.com>" in result
