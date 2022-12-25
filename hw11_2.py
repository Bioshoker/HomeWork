# Реализовать решение «Задачи об обедающих философах»
# «Пять безмолвных философов сидят вокруг круглого стола, перед каждым философом стоит тарелка спагетти.
# Вилки лежат на столе между каждой парой ближайших философов. Каждый философ может либо есть, либо размышлять.
# Прием пищи не ограничен количеством оставшихся спагетти — подразумевается бесконечный запас.
# Тем не менее, философ может есть только тогда, когда держит две вилки — взятую справа и слева
# (альтернативная формулировка проблемы подразумевает миски с рисом и палочки для еды
# вместо тарелок со спагетти и вилок). Каждый философ может взять ближайшую вилку (если она доступна) или положить —
# если он уже держит её. Взятие каждой вилки и возвращение её на стол являются раздельными действиями,
# которые должны выполняться одно за другим. Вопрос задачи заключается в том, чтобы разработать модель поведения
# (параллельный алгоритм), при котором ни один из философов не будет голодать,
# то есть будет вечно чередовать приём пищи и размышления.»


import threading
from time import sleep
import random
forks = 5
philosophers = 5

forks_lock = [threading.Lock() for n in range(forks)]


def philosophers_dinner(right_fork, left_fork, philosopher):
    while True:
        first_fork = min(right_fork, left_fork)
        second_fork = max(right_fork, left_fork)
        forks_lock[first_fork].acquire()
        forks_lock[second_fork].acquire()
        print(f'Философ {philosopher} ест')
        sleep(random.randint(1, 5))
        forks_lock[second_fork].release()
        forks_lock[first_fork].release()


for philosopher in range(philosophers):
    right_fork = philosopher
    left_fork = (philosopher+1) % philosophers
    threading.Thread(target=philosophers_dinner, args=(right_fork, left_fork, philosopher)).start()