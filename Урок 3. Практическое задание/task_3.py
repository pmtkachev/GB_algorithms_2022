"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""
from hashlib import md5


def hash_func(str_, set_):
    for i in range(len(str_) + 1):
        for j in range(i + 1, len(str_) + 1):
            set_.add(md5(str_[i:j].encode('UTF-8')).hexdigest())
    return len(set_) - 1


sett = set()

if __name__ == '__main__':
    print(f'В вашей строке - {hash_func(input("Введите строку: "), sett)} уникальных подстрок')
