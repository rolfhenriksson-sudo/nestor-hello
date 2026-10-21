"""Nestors första program."""
from datetime import date


def halsa(namn: str = "världen") -> str:
    return f"Hej {namn}, från Nestor! Idag är det {date.today().isoformat()}, så det så. Och nu har jag uppaterat texten igen."


if __name__ == "__main__":
    print(halsa())
