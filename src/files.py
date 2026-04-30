import os

UPLOAD_DIR = "/var/app/uploads"


def read_user_file(filename: str) -> str:
    base_dir = os.path.abspath(UPLOAD_DIR)
    path = os.path.abspath(os.path.join(base_dir, filename))
    if os.path.commonpath([base_dir, path]) != base_dir:
        raise ValueError("invalid filename")
    with open(path, "r") as f:
        return f.read()


def delete_user_file(filename: str) -> None:
    base_dir = os.path.abspath(UPLOAD_DIR)
    path = os.path.abspath(os.path.join(base_dir, filename))
    if os.path.commonpath([base_dir, path]) != base_dir:
        raise ValueError("invalid filename")
    os.remove(path)
