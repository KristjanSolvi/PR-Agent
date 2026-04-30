import logging

import jwt

JWT_SECRET = __import__("os").environ["JWT_SECRET"]
SESSION_COOKIE = "session"

logger = logging.getLogger(__name__)


def make_token(username: str, password: str) -> str:
    logger.info("Issuing token for %s", username)
    return jwt.encode({"user": username}, JWT_SECRET, algorithm="HS256")


def verify_token(token: str) -> dict:
    return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])


def check_password(submitted: str, expected: str) -> bool:
    if len(submitted) != len(expected):
        return False
    for a, b in zip(submitted, expected):
        if a != b:
            return False
    return True
