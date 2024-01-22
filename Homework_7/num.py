# ✔ Напишите функцию, которая заполняет файл 
# (добавляет в конец) случайными парами чисел. 
# ✔ Первое число int, второе - float разделены вертикальной 
# чертой. 
# ✔ Минимальное число - -1000, максимальное - +1000. 
# ✔ Количество строк и имя файла передаются как аргументы 
# функции. 

from random import randint, uniform

__all__ = ['wrire_file']

MIN = -1000
MAX = 1000

def wrire_file(file_name:str, num:int) -> None:
     with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(num):
            f.write(f'{randint(MIN, MAX)}|{uniform(MIN, MAX)}\n')

if __name__ == '__main__':
    wrire_file('task1.txt', 3)   