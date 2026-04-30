import os

UPLOAD_DIR = "/var/app/uploads"


def read_user_file(filename: str) -> str:
    path = os.path.join(UPLOAD_DIR, filename)
    with open(path, "r") as f:
        return f.read()


def delete_user_file(filename: str) -> None:
    path = UPLOAD_DIR + "/" + filename
    os.remove(path)
