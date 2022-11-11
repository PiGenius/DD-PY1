from random import sample
from string import ascii_lowercase, ascii_uppercase, digits


def get_random_password(length: int = 8, digits_=True, uppercase=True) -> str:
    available_symbols = ascii_lowercase
    if digits_:
        available_symbols += digits
    if uppercase:
        available_symbols += ascii_uppercase
    return ''.join(sample(available_symbols, length))


print(get_random_password())
