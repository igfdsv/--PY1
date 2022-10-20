def get_count_char(str_):
    frequencies = dict()
    str_ = str_.lower()
    for l in str_:
        if not l.isalpha():
            continue
        if l not in frequencies:
            frequencies[l] = 1
        else:
            frequencies[l] += 1
    return frequencies

def to_percentage(dict_):
    total_letters = sum(dict_.values())
    for l, v in dict_.items():
        dict_[l] = 100 * v / total_letters
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
#print(to_percentage(get_count_char(main_str)))
