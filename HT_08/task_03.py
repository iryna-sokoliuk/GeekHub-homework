"""
Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
Тобто щоб її можна було використати у вигляді:
    for i in my_range(1, 10, 2):
        print(i)
    1
    3
    5
    7
    9
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній:
    https://docs.python.org/3/library/stdtypes.html#range
   P.P.P.S Не забудьте обробляти невалідні ситуації (аналог range(1, -10, 5)).
    Подивіться як веде себе стандартний range в таких випадках.
"""


def my_range(start, stop, step=1):
    if start < stop:
        while start < stop:
            yield start
            start += step
    if start > stop:
        while start > stop:
            yield start
            start -= step
    else:
        return


for i in my_range(0, -10, 1):
    print(i)