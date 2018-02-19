"""Tests for for https://www.codewars.com/kata/number-of-measurements-to-spot-the-counterfeit-coin/"""

import pytest

TESTS = [
    (1, 0),
    (2, 1),
    (3, 1),
    (8, 2),
    (82, 5),
    (100, 5),
]

@pytest.mark.parametrize('coins, result', TESTS)
def test_how_many_measurements(coins, result):
    """Test that function how_many_measurements returns a defined result."""
    from counterfeit import how_many_measurements
    assert how_many_measurements(coins) == result

@pytest.mark.parametrize('coins, result', TESTS)
def test_how_many_measurements(coins, result):
    """Test that function how_many_measurements returns a defined result."""
    from counterfeit import how_many_measurements_short
    assert how_many_measurements_short(coins) == result
