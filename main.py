from src.client import fetch_user
from src.utils.formatter import format_user


def main() -> None:
    user = fetch_user(1)
    print(format_user(user))


if __name__ == "__main__":
    main()
