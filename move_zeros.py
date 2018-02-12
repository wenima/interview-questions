"""Solution for https://www.codewars.com/kata/kata/moving-zeros-to-the-end/"""

def move_zeros(l):
    """Return a list with all zeroes moved to the end while keeping original order
    for all non-zero values."""
    out = []
    for n in l:
        if not any([type(n) is int, type(n) is float]):
            out.append(n)
            continue
        if not int(n) is 0:
            out.append(n)
    return out + (len(l) - len(out)) * [0]
