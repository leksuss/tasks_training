# https://www.codewars.com/kata/52b7ed099cdc285c300001cd


def join_crossed(intv1, intv2):
    if max(intv1[0], intv2[0]) <= min(intv1[1], intv2[1]):
        max_val = max(max(intv1), max(intv2))
        min_val = min(min(intv1), min(intv2))
        return (min_val, max_val)
    return None


def sum_of_intervals(intervals):
    intervals.sort()
    uniq_intvs = [intervals[0]]
    for intv in intervals[1:]:
        new_intv = join_crossed(intv, uniq_intvs[-1])
        if new_intv:
            uniq_intvs[-1] = new_intv
        else:
            uniq_intvs.append(intv)
    return sum(map(lambda x: x[1] - x[0], uniq_intvs))


assert sum_of_intervals([(1, 5)]), 4
assert sum_of_intervals([(1, 5), (6, 10)]), 8
assert sum_of_intervals([(1, 5), (1, 5)]), 4
assert sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7
assert sum_of_intervals([(-1000000000, 1000000000)]), 20000000000
assert sum_of_intervals([(0, 20), (-100000000, 10), (30, 40)]), 100000030
