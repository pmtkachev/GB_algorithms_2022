"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.

Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.

Решите задачу тремя способами:

2) без сортировки

сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit

m = int(input('Введите натуральное число: '))
arr = [randint(0, 100) for i in range(2 * m + 1)]


def get_median(array):
    mid = len(array) // 2
    while len(array) > mid:
        array.remove(max(array))
    return f"Медиана списка {max(array)}"


print(get_median(arr[:]))

print(timeit("get_median(arr[:])", globals=globals(), number=1000))

'''
10 - 0.004389099995023571
100 - 0.08683549999841489
1000 - 7.500772999999754
'''
