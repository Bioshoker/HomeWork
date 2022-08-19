﻿# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [i ** 2 for i in list1]
print(list2)



# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.


fruits_list_1 = ['яблоко', 'мандарин', 'манго', 'груша', 'апельсин', 'нектарин']
fruits_list_2 = ['банан', 'киви', 'яблоко', 'лимон', 'груша', 'ананас', 'мандарин', 'грейпфрут']

fruits_list_3 = [i for i in fruits_list_1 if i in fruits_list_2]
print(fruits_list_3)



# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 20, 27]
list4 = [i for i in list3 if i % 3 == 0 and i > 0 and i % 4 != 0]
print(list4)