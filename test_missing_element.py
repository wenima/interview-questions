"""Tests for https://www.codewars.com/kata/find-the-missing-element-between-two-arrays."""

import pytest

TEST = [
    ([1, 2, 3], [1, 3], 2),
    ([6, 1, 3, 6, 8, 2], [3, 6, 6, 1, 2], 8),
    ([7], [], 7),
    ([4, 3, 3, 61, 8, 8], [8, 61, 8, 3, 4], 3),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0], 0)
]

@pytest.mark.parametrize('source, target, result', TEST)
def test_find_missing(source, target, result):
    """Test that function find_missing returns the missing element between 2 lists."""
    from missing_element import find_missing
    assert find_missing(source, target) == result

@pytest.mark.parametrize('source, target, result', TEST)
def test_find_missing(source, target, result):
    """Test that function find_missing returns the missing element between 2 lists."""
    from missing_element import find_missing_counter
    assert find_missing_counter(source, target) == result
