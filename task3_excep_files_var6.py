import re


str1 = ''

def analize_text(str1):
    str_low = str1.lower()  # приводим строку в lower_case
    reg = re.compile('[^a-zа-я]')
    str_cut = reg.sub('', str_low)  # оставляем только буквы RUS|ENG алфавита, исключая спец.символы и пробелы
    key = set(str_cut)  # формируем множество уникальных букв из строки
    values = (str_cut.count(letter) for letter in key)  # считаем частоту встречаемости буквы в строке str_obrez
    analize = dict(zip(key, values))  # используем zip, объединяем в пары и создаем словарь
    str_out = ''
    for letter_d, frequency_d in analize.items():
        str_out += 'Буква: ' + letter_d + ';  ' + 'Частота: ' + str(frequency_d) + '\n'
    return str_out

try:
    f = open('orig_text.txt')
    str1 = f.read()
    f.close
except FileNotFoundError:
    print("Файл orig_text.txt не найден")
    exit()

#  Mode - x, файл output_analize.txt очень дорог нам
#  защитим его от перезаписи в случае, если он существует.
try:
    with open('output_analize.txt', 'xt') as fout:
        fout.write(analize_text(str1))
except FileExistsError:
    print("Файл output_analize.txt уже существует")
    exit()
