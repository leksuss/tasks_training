#  https://www.codewars.com/kata/52e864d1ffb6ac25db00017f
#  using this algo https://en.wikipedia.org/wiki/Shunting_yard_algorithm

WEIGHT = {
    '^': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    ')': 0,
    '(': 0,
}


def to_postfix(infix):
    postfix = []
    ops = []
    for char in infix:
        if char.isdigit():
            postfix.append(char)
        elif char == '(':
            ops.append(char)
        elif char == ')':
            while ops[-1] != '(':
                postfix.append(ops.pop())
            ops.pop()
        else:
            while ops and WEIGHT[ops[-1]] >= WEIGHT[char] and WEIGHT[char] != 3:
                postfix.append(ops.pop())
            ops.append(char)
    return ''.join(postfix + ops[::-1])


assert to_postfix("2+7*5") == "275*+"
assert to_postfix("3*3/(7+1)") == "33*71+/"
assert to_postfix("5+(6-2)*9+3^(7-1)") == "562-9*+371-^+"
assert to_postfix("(5-4-1)+9/5/2-7/1/7") == "54-1-95/2/+71/7/-"
assert to_postfix("1^2^3") == "123^^"
