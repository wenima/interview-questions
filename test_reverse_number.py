"""Solution for https://www.codewars.com/kata/reverse-a-number"""

import pytest

TESTS = [
    (123, 321),
    (-123, -321),
    (1000, 1),
    (4321234, 4321234),
    (5, 5),
    (98989898, 89898989),
]

@pytest.mark.parametrize('source, result', TESTS)
def test_reverse_number(source, result):
    """Test that function reverse_number returns the correct result."""
    from reverse_number import reverse_number
    assert reverse_number(source) == result

@pytest.mark.parametrize('source, result', TESTS)
def test_reverse_number_short(source, result):
    """Test that function reverse_number returns the correct result."""
    from reverse_number import reverse_number_short
    assert reverse_number_short(source) == result

@pytest.mark.parametrize('source, result', TESTS)
def test_reverse_mod(source, result):
    """Test that function reverse_number returns the correct result."""
    from reverse_number import reverse_number_mod
    assert reverse_number_mod(source) == result
