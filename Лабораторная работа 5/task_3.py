from random import randint


def get_unique_list_numbers(start: int = -10, end: int = 10, length: int = 15) -> list[int]:
    if end < start:
        raise ValueError('Начало диапазона чисел должно быть левее конца!')
    if length > (end - start + 1):
        raise ValueError('Длина списка не может быть больше числа уникальных символов!')
    unique_list_numbers = []
    while len(unique_list_numbers) < length:
        rand_int = randint(start, end)
        if rand_int not in unique_list_numbers:
            unique_list_numbers.append(rand_int)
    return unique_list_numbers


list_unique_numbers = get_unique_list_numbers(1, 2, 10)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
