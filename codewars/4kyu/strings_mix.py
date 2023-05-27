# https://www.codewars.com/kata/5629db57620258aa9d000014/
from collections import Counter


def _filter(s_count):
    abc = tuple(chr(letter) for letter in range(97, 123))
    for char, count in s_count.copy().items():
        if char not in abc or count == 1:
            del s_count[char]
    return s_count


def mix(s1, s2):
    result = []
    s1_count = _filter(Counter(s1))
    s2_count = _filter(Counter(s2))
    for char in s1_count + s2_count:
        if s2_count.get(char, 0) > s1_count.get(char, 0):
            result.append((s2_count.get(char), '2', char))
        elif s1_count.get(char, 0) == s2_count.get(char, 0):
            result.append((s2_count.get(char), '=', char))
        else:
            result.append((s1_count.get(char), '1', char))
    result.sort(key=lambda x: (-x[0], x[1], x[2]))
    return '/'.join(f'{item[1]}:{item[0]*item[2]}' for item in result)


assert mix('Are they here', 'yes, they are here') == '2:eeeee/2:yy/=:hh/=:rr'
assert mix('Sadus:cpms>orqn3zecwGvnznSgacs','MynwdKizfd$lvse+gnbaGydxyXzayp') == '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz'
assert mix('looping is fun but dangerous', 'less dangerous than coding') == '1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg'
assert mix(' In many languages', " there's a pair of functions") == '1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt'
assert mix('Lords of the Fallen', 'gamekult') == '1:ee/1:ll/1:oo'
assert mix('codewars', 'codewars') == ''
assert mix('A generation must confront the looming ', 'codewarrs') == '1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr'
