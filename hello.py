"""Nestors första program."""
from datetime import date


def halsa(namn: str = "världen") -> str:
    return f" {namn}, från Nestor! Idag är det {date.today().isoformat()}, så det så."


if __name__ == "__main__":
    print(halsa())
