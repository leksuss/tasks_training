# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    return n % 9 or n and 9


assert digital_root(16) == 7
assert digital_root(9) == 9
assert digital_root(0) == 0
assert digital_root(132189) == 6
assert digital_root(493193) == 2
