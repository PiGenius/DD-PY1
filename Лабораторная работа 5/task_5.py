from random import sample


def get_random_password(n: int = 8) -> str:
    available_symbols = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + list('abcdefghijklmnopqrstuvwxyz') + list('0123456789')
    symbol_list = sample(available_symbols, n)
    password = ''.join(symbol_list)
    return password


print(get_random_password())
