def get_count_char(str_):
    chars_dict = {}
    default_count = 0
    for char in str_.lower():
        if char.isalpha():
            chars_dict[char] = chars_dict.get(char, default_count) + 1
    result = change_to_percentage(chars_dict)
    return result


def change_to_percentage(dict_):
    total_amount_of_symbols = sum(dict_.values())
    percentages = {}
    max_count = 0
    max_char = ''
    sum_of_percentages = 0
    for char, count in dict_.items():
        percentage = round(count / total_amount_of_symbols * 100, 2)
        sum_of_percentages += percentage
        if count > max_count:
            max_count = count
            max_char = char
        percentages[char] = percentage
    if sum_of_percentages != 100:
        percentages[max_char] += 100 - sum_of_percentages
        percentages[max_char] = round(percentages[max_char], 2)
    return percentages


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
