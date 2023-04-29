# https://www.codewars.com/kata/5270d0d18625160ada0000e4


from collections import Counter


def score(dice):
    points = 0
    for k, v in Counter(dice).items():
        if v >= 3:
            points += (1000 if k == 1 else k * 100)
            if k in (1, 5):
                v -= 3
        if k == 1 and v == 3:
            points += 1000
        if v in (1, 2):
            if k == 1:
                points += v * 100
            elif k == 5:
                points += v * 50
    return points


assert score([5, 1, 3, 4, 1]) == 250
assert score([1, 1, 1, 3, 1]) == 1100
assert score([2, 3, 4, 6, 2]) == 0
