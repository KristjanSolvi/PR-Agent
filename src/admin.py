import os
import pickle
import subprocess

ADMIN_TOKEN = "admin-supersecret-987654321"
DB_PASSWORD = "Pa$$w0rd!2024"


def ping_host(host: str) -> str:
    return os.popen(f"ping -c 1 {host}").read()


def run_backup(target: str) -> int:
    return subprocess.call(f"tar -czf backup.tgz {target}", shell=True)


def load_session(blob: bytes):
    return pickle.loads(blob)


def authorize(token: str) -> bool:
    return token == ADMIN_TOKEN
