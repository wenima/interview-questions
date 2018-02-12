"""Tests for for https://www.codewars.com/kata/kata/moving-zeros-to-the-end/"""

import pytest

TESTS = [
    ([1,2,0,1,0,1,0,3,0,1], [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]),
    ([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9], [9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]),
    (["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9], ["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0]),
    (["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9], ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0]),
    ([0,1,None,2,False,1,0], [1,None,2,False,1,0,0]),
    (["a","b"], ["a","b"]),
    (["a"], ["a"]),
    ([0,0], [0,0]),
    ([0], [0]),
    ([], []),
]

@pytest.mark.parametrize('source, result', TESTS)
def test_move_zeros(source, result):
    """Test that function move_zeros returns a list matching result."""
    from move_zeros import move_zeros
    assert move_zeros(source) == result
