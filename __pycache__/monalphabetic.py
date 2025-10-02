import string

alphabet = string.ascii_uppercase
cipher_alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"

mono_dict = dict(zip(alphabet,cipher_alphabet))

def encrypt(text, mapping):
    text = text.upper()
    return ''.join(mapping.get(ch, ch) for ch in text)