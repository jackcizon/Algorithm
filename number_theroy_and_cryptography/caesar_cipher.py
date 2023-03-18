from pathlib import Path

#convert:
    #(char - 'a' + shift) % 26 + 'a'

def encrypto(text, shift):
    cipher = ""

    for i in range(len(text)):
        char = text[i]

        if char == ' ':
            cipher += ' '

        elif char == '.':
            cipher += '.'

        elif char == ',':
            cipher += ','

        elif char == '?':
            cipher += '?'

        elif char == '\"' or char == '\'':
            cipher += '\"'

        elif char == 'a':
            cipher += '!'

        elif char == 'e':
            cipher += '@'

        elif char == 'i':
            cipher += '$'

        elif char == 'o':
            cipher += '%'

        elif char == 'u':
            cipher += '^'

        elif char == 'b':
            cipher += '&'

        elif char == 'f':
            cipher += '*'

        elif char == 'j':
            cipher += '('

        elif char == 'p':
            cipher += ')'

        elif char == 'v':
            cipher += '-'

        elif char == 'x':
            cipher += '='

        elif char == 'y':
            cipher += '+'

        elif char == 'z':
            cipher += '/'

        elif char.isdigit():
            cipher += char

        elif char.isupper():
            cipher += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))

        elif char.islower():
            cipher += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))

        else:
            cipher += char

    return cipher


def decrypto(cipher, shift):
    text = ""

    for i in range(len(cipher)):
        char = cipher[i]

        if char == ' ':
            text += ' '

        elif char == '.':
            text += '.'

        elif char == ',':
            text += ','

        elif char == '?':
            text += '?'

        elif char == '\"' or char == '\'':
            text += '\"'

        elif char == '!':
            text += 'a'

        elif char == '@':
            text += 'e'

        elif char == '$':
            text += 'i'

        elif char == '%':
            text += 'o'

        elif char == '^':
            text += 'u'

        elif char == '&':
            text += 'b'

        elif char == '*':
            text += 'f'

        elif char == '(':
            text += 'j'

        elif char == ')':
            text += 'p'

        elif char == '-':
            text += 'v'

        elif char == '=':
            text += 'x'

        elif char == '+':
            text += 'y'

        elif char == '/':
            text += 'z'

        elif char.isdigit():
            text += char

        elif char.isupper():
            text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))

        elif char.islower():
            text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))

        else:
            text += char

    return text


def main():

    shift = 4

    text = 'text.txt'
    cipher = 'cipher.txt'
    plain = 'plain.txt'

    read = 'r'
    append = 'a'


    print("\n{} in sys path ==>> {}\{}\n".format(text, Path.cwd(), text))


    with open(text, read) as fir, open(cipher, append) as sec:
        for c in fir:
            sec.write(encrypto(c, shift))

    print("\n{} has created in path ==>> {}\{}\n".format(cipher, Path.cwd(), cipher))


    with open(cipher, read) as fir, open(plain, append) as sec:
        for c in fir:
            sec.write(decrypto(c, shift))

    print("\n{}(decrypto) has created in path ==>> {}\{}\n".format(plain, Path.cwd(), plain))



if __name__ == '__main__':
    main()
