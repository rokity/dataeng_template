from datetime import date


class EasterCalculator:
    """
    Class to calculate the date of Easter for a given year using the
    Anonymous Gregorian algorithm (also known as the Meeus/Jones/Butcher algorithm).
    """

    def __init__(self, year: int = None):
        self.year = year or date.today().year

    def get_easter_date(self) -> date:
        """Compute the date of Easter Sunday for the current year."""
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
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = (a + 11 * h + 22 * l) // 451
        month = (h + l - 7 * m + 114) // 31
        day = ((h + l - 7 * m + 114) % 31) + 1

        return date(y, month, day)
