# ✔ Создайте функцию, которая создаёт файлы с указанным 
# расширением. 
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, 
# по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, 
# по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, 
# по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, 
# по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного 
# диапазона.

# ✔ Доработаем предыдущую задачу. 
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями. 
# ✔ Расширения и количество файлов функция принимает в качестве параметров. 
# ✔ Количество переданных расширений может быть любым. 
# ✔ Количество файлов для каждого расширения различно. 
# ✔ Внутри используйте вызов функции из прошлой задачи.


# ✔ Дорабатываем функции из предыдущих задач. 
# ✔ Генерируйте файлы в указанную директорию — отдельный 
# параметр функции. 
# ✔ Отсутствие/наличие директории не должно вызывать 
# ошибок в работе функции 
# (добавьте проверки). 
# ✔ Существующие файлы не должны удаляться/изменяться 
# в случае совпадения имён.


from random import randint, choice
from os import getcwd, mkdir, listdir

__all__ = ['create_file', 'create_random']


VOWES = 'aeiouy'
CONSTONATS = 'bcdfghjklmnqrstvwxz'
EXTEN = ['.txt', '.doc', '.pdf', '.csv']

def give_name(min_num, max_num) ->str:
    res = ''.join(choice(VOWES) if i % 3 == 0 else choice(CONSTONATS)
                                 for i in range(1, randint(min_num, max_num)))
    return res


def create_file(ext: str, directory: str = None, min_name: int = 6, 
                max_name: int = 30, min_byte: int = 256, 
                max_byte: int = 4096, count: int = 42) -> None:
    if not directory:
        directory = getcwd() + '\\'
    else:
        if directory not in listdir():
            mkdir(directory)
        directory = getcwd() + '\\' + directory + '\\'
    for _ in range(count):                              
        with open(directory + give_name(min_name, max_name + 1) + 
                  ext, 'wb') as f:
            data = bytes(randint(0, 255) for _ in range(min_byte, max_byte))
            f.write(data)


def create_random() -> None:
    ext = choice(EXTEN)
    create_file(ext)

if __name__ == '__main__':
    create_file(ext=choice(EXTEN), directory='test_dir', 
                min_name=5, max_name= 7, count=5)