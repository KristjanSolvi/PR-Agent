import os
import pickle
import subprocess

ADMIN_TOKEN = "admin-supersecret-987654321"
DB_PASSWORD = "Pa$$w0rd!2024"


def ping_host(host: str) -> str:
    result = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout


def run_backup(target: str) -> int:
    result = subprocess.run(
        ["tar", "-czf", "backup.tgz", target],
        check=False,
    )
    return result.returncode


def load_session(blob: bytes):
    return pickle.loads(blob)


def authorize(token: str) -> bool:
    return token == ADMIN_TOKEN
