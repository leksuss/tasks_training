# https://www.codewars.com/kata/5544c7a5cb454edb3c000047

def bouncing_ball(h, bounce, window):
    if all([h > 0, 0 < bounce < 1, h > window]):
        jump_height = h * bounce
        count_seen = 1
        while jump_height > window:
            jump_height = jump_height * bounce
            count_seen += 2
        return count_seen
    return -1


assert bouncing_ball(2, 0.5, 1) == 1
assert bouncing_ball(3, 0.66, 1.5) == 3
assert bouncing_ball(30, 0.66, 1.5,) == 15
assert bouncing_ball(30, 0.75, 1.5) == 21
