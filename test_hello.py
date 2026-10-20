from datetime import date

from hello import halsa


def test_halsar_pa_namn():
    assert "Hej Rolf" in halsa("Rolf")


def test_visar_dagens_datum():
    assert date.today().isoformat() in halsa()
