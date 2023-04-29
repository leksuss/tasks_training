# https://www.codewars.com/kata/550498447451fbbd7600041c

def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    squared = sorted(num**2 for num in array1)
    return squared == sorted(array2)


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
assert comp(a1, a2) is True

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
assert comp(a1, a2) is False

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
assert comp(a1, a2) is False
