"""Nestors första program."""


def halsa(namn: str = "världen") -> str:
    return f"Hej {namn}, från Nestor!"


if __name__ == "__main__":
    print(halsa())
