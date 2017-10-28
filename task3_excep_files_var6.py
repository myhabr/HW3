import re
stroka = ''

def analize_text(str1):
    str_low = str1.lower()  # приводим строку в lower_case
    reg = re.compile('[^a-zа-я]')
    str_obrez = reg.sub('', str_low)  # оставляем только буквы RUS|ENG алфавита, исключая спец.символы и пробелы
    key = set(str_obrez)  # формируем множество уникальных букв из строки
    values = (str_obrez.count(letter) for letter in key)  # считаем частоту встречаемости буквы в строке str_obrez
    analize = dict(zip(key, values))  # используем zip, объединяем в пары и создаем словарь
    str_out = ''
    for letter_d, frequency_d in analize.items():
        str_out += 'Буква: ' + letter_d + ';  ' + 'Частота: ' + str(frequency_d) + '\n'
    return str_out

try:
    f = open('orig_text.txt', 'rt')
    chunk = 2000  # читаю буфером
    while True:
        fragment = f.read(chunk)
        if not fragment:
            break
        stroka += fragment  # формируем итоговую строку
    f.close()
except FileNotFoundError:
    print("Файл orig_text.txt не найден")
    exit()

#  Mode - x, файл output_analize.txt очень дорог нам
#  защитим его от перезаписи в случае, если он существует.
try:
    with open('output_analize.txt', 'xt') as fout:
        fout.write(analize_text(stroka))
except FileExistsError:
    print("Файл output_analize.txt уже существует")
    exit()