# https://www.codewars.com/kata/596f610441372ee0de00006e


def de_nico(key, msg):
    new_order = [sorted(key).index(char) for char in key]
    res = ''
    while msg:
        res += ''.join(msg[:len(key)][i] for i in new_order if i < len(msg))
        msg = msg[len(key):]
    return res.rstrip()


assert de_nico('crazy', 'cseerntiofarmit on  ') == 'secretinformation'
assert de_nico('crazy', 'cseerntiofarmit on') == 'secretinformation'
assert de_nico('abc', 'abcd') == 'abcd'
assert de_nico('ba', '2143658709') == '1234567890'
assert de_nico('a', 'message') == 'message'
assert de_nico('key', 'eky') == 'key'
assert de_nico('luacfxsbz', 'yupcisyxztqzkaytocroqxlqksqzwebwqlmred') == 'iyypcxsuzattzkoyqclkrqxsqoqwlzebmqwred'
