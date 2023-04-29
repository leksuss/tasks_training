# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

import operator


def common_oper(oper_num2, num1):
    if oper_num2:
        oper, num2 = oper_num2
        return oper(num1, num2)
    else:
        return num1


def zero(oper_num2=None):
    return common_oper(oper_num2, 0)


def one(oper_num2=None):
    return common_oper(oper_num2, 1)


def two(oper_num2=None):
    return common_oper(oper_num2, 2)


def three(oper_num2=None):
    return common_oper(oper_num2, 3)


def four(oper_num2=None):
    return common_oper(oper_num2, 4)


def five(oper_num2=None):
    return common_oper(oper_num2, 5)


def six(oper_num2=None):
    return common_oper(oper_num2, 6)


def seven(oper_num2=None):
    return common_oper(oper_num2, 7)


def eight(oper_num2=None):
    return common_oper(oper_num2, 8)


def nine(oper_num2=None):
    return common_oper(oper_num2, 9)


def plus(num2):
    return operator.add, num2


def minus(num2):
    return operator.sub, num2


def times(num2):
    return operator.mul, num2


def divided_by(num2):
    return operator.floordiv, num2


assert seven(times(five())) == 35
assert four(plus(nine())) == 13
assert eight(minus(three())) == 5
assert six(divided_by(two())) == 3
