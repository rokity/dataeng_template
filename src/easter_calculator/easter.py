from datetime import date


class EasterCalculator:
    """Calculate the date of Easter Sunday for a given year.

    Uses the Anonymous Gregorian algorithm (also known as
    the Meeus/Jones/Butcher algorithm).
    """

    def __init__(self, year: int = None) -> None:
        self.year = year or date.today().year

    def get_easter_date(self) -> date:
        """Compute the date of Easter Sunday."""
        y = self.year
        a = y % 19
        b = y // 100
        c = y % 100
        d = b // 4
        e = b % 4
        f = (b + 8) // 25
        g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        kappa = c % 4
        temp_l = (32 + 2 * e + 2 * i - h - kappa) % 7  # renamed from `l`
        m = (a + 11 * h + 22 * temp_l) // 451
        month = (h + temp_l - 7 * m + 114) // 31
        day = ((h + temp_l - 7 * m + 114) % 31) + 1
        return date(y, month, day)
