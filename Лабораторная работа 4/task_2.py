def get_count_char(str_):
    chars_dict = {}
    default_count = 0
    for char in str_.lower():
        if char.isalpha():
            chars_dict[char] = chars_dict.get(char, default_count) + 1
    #result = change_to_percentage(chars_dict)
    return chars_dict


def change_to_percentage(dict_):
    length_of_string = sum(dict_.values())
    for char, count in dict_.items():
        dict_[char] = round(count / length_of_string * 100, 1)
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
