"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def calc(operand, num_1, num_2):
    if operand == '0':
        return 'Завершение'
    if operand in ['+', '-', '*', '/']:
        if num_1.isdigit() and num_2.isdigit():
            try:
                print(f'Результат: {eval(num_1 + operand + num_2)}')
            except ZeroDivisionError:
                print('На ноль делить нельзя!')
        else:
            print('Аргументы должны быть числами!')
    else:
        print('Введен неверный знак, попробуйте еще раз!')
    return calc(input('Введите операцию (+, -, *, / или 0 для выхода): '),
                input('Введите первое число: '),
                input('Введите второе число: '))


if __name__ == '__main__':
    print(calc(input('Введите операцию (+, -, *, / или 0 для выхода): '),
               input('Введите первое число: '),
               input('Введите второе число: ')))
