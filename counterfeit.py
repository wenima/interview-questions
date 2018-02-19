"""Tests for for https://www.codewars.com/kata/number-of-measurements-to-spot-the-counterfeit-coin/"""

from math import ceil

def how_many_measurements(n):
    """Return the number of measurements it would take to find the counterfeit coin within n coins."""
    if n == 1: return 0
    if n in [2, 3]: return 1
    if n < 10: return 2
    i = 0
    while n > 9:
        i += 1
        n = ceil(n / 3)
    return i + 2
