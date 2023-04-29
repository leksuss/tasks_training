# https://www.codewars.com/kata/520446778469526ec0000001
# unlimited-nested-lists version of this kata solution
#
# isinstance check in return should cover
# strange test case in codewars: same_structure_as([], 1)

def same_structure_as(original, other):
    def go_deeper(lst, is_flat=False):
        if is_flat:
            return [1] * len(lst)
        is_flat = True
        for i, item in enumerate(lst):
            if isinstance(item, list):
                go_deeper(item, False)
            else:
                lst[i] = 1
        return lst
    return (isinstance(original, list)
            and isinstance(other, list)
            and go_deeper(original) == go_deeper(other))


assert same_structure_as([], [[], []]) is False
assert same_structure_as([], 1) is False
assert same_structure_as([1, [1, 1]], [2, [2, 2]]) is True
assert same_structure_as([1, [1, 1]], [[2, 2], 2]) is False
assert same_structure_as([1], [[1]]) is False
