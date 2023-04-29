# https://www.codewars.com/kata/55c04b4cc56a697bb0000048
# this soltion works with from Python 3.10

from collections import Counter


def scramble(s1, s2):
    return Counter(s1) >= Counter(s2)


assert scramble('rkqodlw', 'world') is True
assert scramble('cedewaraaossoqqyt', 'codewars') is True
assert scramble('katas', 'steak') is False
assert scramble('scriptjava', 'javascript') is True
assert scramble('scriptingjava', 'javascript') is True
assert scramble('abcdefghijklmnopqrstuvwxyz' * 10000, 'zyxcba' * 9000) is True
assert scramble('rkqodlw', 'world') is True
