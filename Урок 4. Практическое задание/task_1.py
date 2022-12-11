"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


print(timeit(stmt="func_1([1,2,3,4,5,6,7,8,9,10])", setup="from __main__ import func_1",
             number=1000000))


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


print(timeit(stmt="func_2([1,2,3,4,5,6,7,8,9,10])", setup="from __main__ import func_2",
             number=1000000))

# Время выполнения в первом случае: 1.4674752000137232
# Во второй функции: 1.2459012999897823
# В своей версии функции я воспользовался List Comprehensions
# Без объявления лишних переменных, тем самым скорость немного повысилась
