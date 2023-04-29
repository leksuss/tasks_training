# https://www.codewars.com/kata/52223df9e8f98c7aa7000062


def rot13(message):
    def decode(char):
        ansi_num = ord(char.lower())
        if ansi_num in range(97, 123):
            rot13_char = chr((ansi_num - 84) % 26 + 97)
            return rot13_char.upper() if char.isupper() else rot13_char
        return char
    return ''.join(decode(char) for char in message)


assert rot13('EBG13 rknzcyr.') == 'ROT13 example.'
assert rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf.") == "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes."
assert rot13('123') == '123'
assert rot13('Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)') == 'This is actually the first kata I ever made. Thanks for finishing it! :)'
assert rot13('@[`{') == '@[`{'
