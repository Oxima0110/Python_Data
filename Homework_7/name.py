# ✔ Напишите функцию, которая генерирует 
# псевдоимена. 
# ✔ Имя должно начинаться с заглавной буквы, 
# состоять из 4-7 букв, среди которых 
# обязательно должны быть гласные. 
# ✔ Полученные имена сохраните в файл.

from pathlib import Path
from random import randint, choice

__all__ = ['get_name']

VOWES = 'aeiouy'
CONSTONATS = 'bcdfghjklmnqrstvwxz'


def get_name(count: int, name_len_min: int, name_len_max: int, file_2: Path) -> None:
    with open(file_2, 'a', encoding='utf-8') as f_2:
        for _ in range(count):
            rad_string = ''.join(choice(VOWES) if i % 3 == 0 else choice(CONSTONATS)
                                 for i in range(1, randint(name_len_min + 1, name_len_max + 1)))
            f_2.write(f'{rad_string.capitalize()}\n')


if __name__ == '__main__':
    get_name(5, 3, 7, 'task2.txt')
