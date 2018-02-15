"""Solution for https://www.codewars.com/kata/reverse-a-number"""

def reverse_number(n):
    """Return a given number in reverse while keeping the sign."""
    n = str(n)
    return int(n[0] + n[1:][::-1] if n[0] in ['-', '+'] else n[::-1])

#if only negative numbers carry a sign and cast to string is allowed
def reverse_number_short(n):
    if n < 0: return -reverse_number(-n)
    return int(str(n)[::-1])

#using mod
def reverse_number_mod(n):
    reverse = 0
    if n >= 0:
        while n:
            last_digit = n % 10
            reverse = (reverse * 10) + last_digit
            n //= 10
        return reverse
    else:
        return -(reverse_number(abs(n)))
