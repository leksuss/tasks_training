# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3

class VigenereCipher(object):

    def __init__(self, key, alphabet):
        self.key = key
        self.abc = alphabet

    def transform(self, txt, operator=1):
        long_key = (self.key * int(len(txt) / len(self.key) + 1))[:len(txt)]
        transform_txt = list(map(self.abc.index, long_key))
        for i, char in enumerate(txt):
            if char in self.abc:
                new_pos = self.abc.index(char) + operator * transform_txt[i]
                char = self.abc[new_pos % len(self.abc)]
            transform_txt[i] = char
        return ''.join(transform_txt[:len(txt)])

    def encode(self, txt):
        return self.transform(txt, 1)

    def decode(self, txt):
        return self.transform(txt, -1)


abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)

assert c.encode('codewars'), 'rovwsoiv'
assert c.decode('rovwsoiv'), 'codewars'

assert c.encode('waffles'), 'laxxhsj'
assert c.decode('laxxhsj'), 'waffles'

assert c.encode('CODEWARS'), 'CODEWARS'
assert c.decode('CODEWARS'), 'CODEWARS'
