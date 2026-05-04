import re

EMAIL_RE = re.compile(r"^([a-zA-Z0-9_.+-]+)+@([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$")


def is_valid_email(value: str) -> bool:
    return bool(EMAIL_RE.match(value))


_attempts: dict[str, int] = {}


def record_attempt(ip: str) -> int:
    _attempts[ip] = _attempts.get(ip, 0) + 1
    return _attempts[ip]
