"""Solution for https://www.codewars.com/kata/kata/moving-zeros-to-the-end/"""

def move_zeros(l):
    """Return a list with all zeroes moved to the end while keeping original order
    for all non-zero values."""
    out = [n for n in l if n != 0]
    return out + (len(l) - len(out)) * [0]
