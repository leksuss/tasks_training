# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34

import math


def zeros(n):
    if n:
        k, k_max = 1, math.log(n, 5)
        count_of_zeros = 0
        while k < k_max:
            count_of_zeros += math.floor(n / 5**k)
            k += 1
        return count_of_zeros
    return n


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
