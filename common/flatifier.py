def flatifier(lst, is_flat=False):
    """Makes flat list from any nested lists"""
    if is_flat:
        return lst
    flatter_lst, is_flat = [], True
    for item in lst:
        if isinstance(item, list):
            flatter_lst.extend(item)
            is_flat = False
        else:
            flatter_lst.append(item)
    return flatifier(flatter_lst, is_flat)


assert flatifier([1, [1, [4, [5]]]]) == [1, 1, 4, 5]
assert flatifier([], [[], []]) == []
assert flatifier([]) == []
assert flatifier([1]) == [1]
assert flatifier([[[1]]]) == [1]
assert flatifier([[[1, 2]]]) == [1, 2]
assert flatifier([1, [1, 1]]) == [1, 1, 1]
