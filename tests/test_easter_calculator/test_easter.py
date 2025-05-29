from datetime import date

import pytest

from easter_calc.easter import EasterCalculator


@pytest.mark.parametrize(
    ("year", "expected"),
    [
        (2024, date(2024, 3, 31)),
        (2025, date(2025, 4, 20)),
        (2026, date(2026, 4, 5)),
        (2030, date(2030, 4, 21)),
        (2000, date(2000, 4, 23)),
    ],
)
def test_get_easter_date(year: int, expected: date) -> None:
    calc = EasterCalculator(year)
    assert calc.get_easter_date() == expected


def test_default_year(monkeypatch) -> None:
    class FakeDate:
        @staticmethod
        def today():
            return date(2025, 1, 1)

    monkeypatch.setattr("easter_calc.easter.date", FakeDate)
    calc = EasterCalculator()
    assert isinstance(calc.get_easter_date(), date)
