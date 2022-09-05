# caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message with no space in between:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text1, shift1):
    new_cipher = ""
    for letter in text1:
        pos = alphabet.index(letter)
        new_pos = pos + shift1
        new_string = alphabet[new_pos]
        new_cipher += new_string
    print(new_cipher)


def decrypt(new_cipher, shift1):
    plain_text = ""
    for letter in new_cipher:
        pos = alphabet.index(letter)
        new_pos = pos - shift1
        new_string = alphabet[new_pos]
        plain_text += new_string
    print(plain_text)


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("wrong entry")
