# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили
# def convert(km):
# print(miles)

km = int(input('Введите кол-во километров: '))
def convert(km):
    miles = km / 1.609
    print(miles)
convert(km)

# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def f(n=float(input("Введите число: "))):
    if float(n) - int(n) > 0.5:
        print(int(n) + 1)
    else:
        print(int(n))
f()



# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    if len(ticket_number) != 6:
        return False
    first_part = ticket_number[0:3]
    second_part = ticket_number[3:6]
    sum_first_part = 0
    for i in first_part:
        sum_first_part = sum_first_part + int(i)
    sum_second_part = 0
    for i in second_part:
        sum_second_part = sum_second_part + int(i)
    if sum_first_part == sum_second_part:
        return True
    else:
        return False