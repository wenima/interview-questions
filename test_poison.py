"""Tests for for  https://www.codewars.com/kata/whats-your-poison."""

import pytest

TESTS = [
    ([0,3,5,4,9,8],825),
    ([0,1,9,3,5],555),
    ([0,1,2,3,4,6],95),
    ([0,1,3,4],27),
]

@pytest.mark.parametrize('deadrats, result', TESTS)
def find(deadrats, result):
    """Test that function find returns the number of the poisoned bottle."""
    from poison import find
    assert find(deadrats) == result
