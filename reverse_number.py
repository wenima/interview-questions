"""Solution for https://www.codewars.com/kata/reverse-a-number"""

def reverse_number(n):
    """Return a given number in reverse while keeping the sign."""
    n = str(n)
    return int(n[0] + n[1:][::-1] if n[0] in ['-', '+'] else n[::-1])
