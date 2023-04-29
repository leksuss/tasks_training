# https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c


def max_sequence(arr):
    max_sum = current_sum = 0
    for num in arr:
        current_sum = max(0, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


assert max_sequence([]) == 0
assert max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]) == 0
assert max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]) == 155
