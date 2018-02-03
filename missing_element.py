"""Solution for https://www.codewars.com/kata/find-the-missing-element-between-two-arrays/"""

from collections import Counter

#without imports from std lib
def find_missing(arr1, arr2):
    """Return the missing element between arr1 and arr2."""
    diff = set(arr1) - set(arr2)
    if diff:
        return list(diff)[0]
    else:
        d_arr1 = {n : 0 for n in arr1}
        d_arr2 = {n : 0 for n in arr2}
        for n in arr1:
            d_arr1[n] += 1
        for n in arr2:
            d_arr2[n] += 1
        for n in arr1:
            if d_arr1[n] != d_arr2[n]:
                return n

#using Counter from collections
def find_missing_counter(arr1, arr2):
    """Return the missing element between arr1 and arr2 using Counter."""
    c_arr1 = Counter(arr1)
    c_arr2 = Counter(arr2)
    return list(set(c_arr1.items()) - set(c_arr2.items()))[0][0]
