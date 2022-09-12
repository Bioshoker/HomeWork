# Задача-1:
# Примечание: Если уже делали easy задание, то просто перенесите решение сюда.
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5


a = float(input("a = "))
b = float(input("b = "))
c = avg(a, b)
print("Среднее геометрическое = {:.2f}".format(c))

# Решение

def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.

    Исключения:
        - ValueError: вычисление не возможно.
    """
    if a * b >= 0:
        return (a * b) ** 0.5
    else:
        raise ValueError("Невозможно определить среднее геометрическое "
                         "введенных чисел.")


try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError:
    print("Пользоватеть введите только числа")

# ПРИМЕЧАНИЕ: Для решения задачи 2-3 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь "меню" выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys


def make_dir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print('Невозможно создать')
    else:
        print('Успешно созадана')


def delete_dir(path):
    try:
        os.rmdir(path)
    except FileNotFoundError:
        print('Невозможно удалить')
    else:
        print('Успешно удалена')


def show_dir():
    for root, dirs, files in os.walk(os.getcwd()):
        for directory in dirs:
            print(directory)
        for item in files:
            print(item)


def go_to_dir(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print('Невозможно перейти')
    else:
        print('Успешно перешёл')


def main():
    menu = """
    Выберите действие (Выбор: '1'-'4' Выход: 'q'):
    1. Перейти в папку
    2. Просмотреть содержимое текущей папки
    3. Удалить папку
    4. Создать папку 
    """

    do = {
        '1': go_to_dir,
        '2': show_dir,
        '3': delete_dir,
        '4': make_dir
    }

    while True:
        print(menu)
        menu_item = input()
        if menu_item == 'q':
            sys.exit()
        action = do.get(menu_item)
        print(action)
        if action == None:
            print('Действие невозможно')
        if menu_item == '2':
            action()
        else:
            path = input('Введите путь к папке: ')
            action(path)


if __name__ == '__main__':
    main()