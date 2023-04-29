# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

def sort_array(source_array):
    to_sort = []
    for i, num in enumerate(source_array):
        if num % 2:
            source_array[i] = None
            to_sort.append(num)
    to_sort.sort(reverse=True)
    for i, num in enumerate(source_array):
        if num is None:
            source_array[i] = to_sort.pop()
    return source_array


assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
assert sort_array([5, 3, 1, 8, 0]) == [1, 3, 5, 8, 0]
assert sort_array([]) == []
