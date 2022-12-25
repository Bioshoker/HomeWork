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