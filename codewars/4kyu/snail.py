# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1


def snail(snail_map):
    res = []
    while snail_map:
        res.extend(snail_map.pop(0))
        snail_map = list(reversed(list(zip(*snail_map))))
    return res


array = [[]]
expected = []
assert snail(array) == expected


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
assert snail(array) == expected


array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert snail(array) == expected
