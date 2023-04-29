# https://www.codewars.com/kata/54d7660d2daf68c619000d95

import math


def convert_fracts(lst):
    lcm = math.lcm(*[n2 for n1, n2 in lst])
    return [[n1 * lcm // n2, lcm] for n1, n2 in lst]


assert convert_fracts([]) == []
assert convert_fracts([[1, 2], [1, 3], [1, 4]]) == [[6, 12], [4, 12], [3, 12]]
