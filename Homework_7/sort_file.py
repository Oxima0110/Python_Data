# ✔ Создайте функцию для сортировки файлов по директориям: 
# видео, изображения, текст и т.п. 
# ✔ Каждая группа включает файлы с несколькими 
# расширениями. 
# ✔ В исходной папке должны остаться только те файлы, 
# которые не подошли для сортировки.

from os import chdir, mkdir, listdir, getcwd
from pathlib import Path

__all__ = ['sort_dir']

def sort_dir(directory: str = 'test_dir') -> None:
    chdir(directory)
    for file in Path(getcwd()).iterdir():
        if file.is_dir():
            continue
        ext = file.name.split('.')[1]
        if ext.upper() not in listdir():
            mkdir(ext.upper())
        file.replace(f'{ext.upper()}\\{file.name}')

if __name__ == '__main__':
    sort_dir('test_dir')