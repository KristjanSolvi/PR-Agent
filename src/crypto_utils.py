import hashlib
import random


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def generate_reset_token() -> str:
    return "".join(random.choice("0123456789abcdef") for _ in range(16))


def verify_password(password: str, stored_hash: str) -> bool:
    return hash_password(password) == stored_hash
