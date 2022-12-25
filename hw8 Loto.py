"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

import random


class Game:
    def __init__(self):
        self.user = User()
        self.comp = Komp()

    def start(self):
        game_is_finished = False
        bochonki = []
        while not game_is_finished:
            new_number = None
            is_unic = False
            while not is_unic:
                new_number = random.randint(1, 90)
                if new_number not in bochonki:
                    is_unic = True
                    bochonki.append(new_number)
            print(new_number)

            answer = input('У вас есть такой номер?' )
            if new_number in self.user.bilet.numbers and answer in ('yes'):
                self.user.bilet.numbers.remove(new_number)
            elif new_number in self.user.bilet.numbers and answer in ('no'):
                print('Игрок проиграл! У него был такой бочонок.')
                game_is_finished = True

            else:
                pass

            if new_number in self.user.bilet.numbers:
                self.user.bilet.numbers.remove(new_number)

            if new_number in self.comp.bilet.numbers:
                self.comp.bilet.numbers.remove(new_number)

            if len(bochonki) == 90 or len(self.user.bilet.numbers) == 0 or len(self.comp.bilet.numbers) == 0:
                game_is_finished = True

    def show_winner(self):
        if len(self.comp.bilet.numbers) == 0 and len(self.user.bilet.numbers) == 0:
            print('Ничья!')
        elif len(self.comp.bilet.numbers) == 0:
            print('Компьютер победил!')
        elif len(self.user.bilet.numbers) == 0:
            print('Игрок победил!')

class User():
    def __init__(self):
        self.bilet = Bilet()
        print(self.bilet.numbers)


class Komp():
    def __init__(self):
        self.bilet = Bilet()
        print(self.bilet.numbers)


class Bilet:
    def __init__(self):
        self.numbers = []
        for i in range(0, 15):
            is_unic = False
            while not is_unic:
                new_number = random.randint(1, 90)
                if new_number not in self.numbers:
                    is_unic = True
                    self.numbers.append(new_number)


game = Game()
game.start()
game.show_winner()
