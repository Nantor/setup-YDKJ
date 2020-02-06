from datetime import date, timedelta


def first_advent(year):
    """ Date of the first advent for the given year."""
    xmas = date(year, 12, 24)
    return xmas - timedelta(days=xmas.isoweekday() % 7, weeks=3)


def spencer_easter_formula(year):
    """ Calculate the date of the easter sunday for the given date"""
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    j = c % 4
    k = (32 + 2 * e + 2 * i - h - j) % 7
    m = (a + 11 * h + 22 * k) // 451
    n = (h + k - 7 * m + 114) // 31
    o = (h + k - 7 * m + 114) % 31
    return date(year, n, o + 1)
