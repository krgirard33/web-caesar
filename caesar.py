def alphabet_position(letter):
    position = ''
    for i in letter:
            position = ord(i.lower()) - 97
    return position


def rotate_character(letter, rot):
    shift = 65 if letter.isupper() else 97
    return chr((ord(letter) + rot - shift) % 26 + shift)


def encrypt(text, rot):
    encrypted = []
    rot = int(rot)
    for symbol in text:
        if symbol.isalpha():
            encrypted.append(rotate_character(symbol, rot))
        else:
            encrypted.append(symbol)

    return ''.join(encrypted)

