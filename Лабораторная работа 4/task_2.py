def get_count_char(str_):
    chars_dict = {}
    default_count = 0
    for char in str_.lower():
        if char.isalpha():
            chars_dict[char] = chars_dict.get(char, default_count) + 1
    #result = change_to_percentage(chars_dict)
    return chars_dict


def change_to_percentage(dict_):
    total_amount_of_symbols = sum(dict_.values())
    changed_dict = {}
    for char, count in dict_.items():
        changed_dict[char] = round(count / total_amount_of_symbols * 100, 1)
    return changed_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
