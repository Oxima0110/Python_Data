# Напишите функцию, которая получает на вход директорию и 
# рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий 
# размер файлов в ней с учётом всех вложенных файлов и 
# директорий.

# Пример:
# test/users/names.txt
# Результат в json для names.txt:
# {
# "name": names.txt
# "parent": users,
# "type": "file"
# "size": 4096
# }

# 3.Соберите из созданных на уроке и в рамках домашнего 
# задания функций пакет для работы с файлами разных форматов.


# Дополнительно:
# Решить задания, которые не успели решить на семинаре(6, 7)


import csv
import json
import os
import pickle

__all__ = ['write_info']
        
def get_info(dir:str, data:list)-> None:
    for i in os.listdir(dir):
        path = dir + '\\' + i
        if os.path.isfile(path):
            data.append({'name':i, 'type':'file', 'size':os.path.getsize(path),
                         'files':None, 'parent':path.split('\\')[-2]})
        if os.path.isdir(path):
            data.append({'name':i, 'type':'folder', 'size':None,
                         'files':len(os.listdir(path)), 'parent':None})
            get_info(path, data)



def write_info(dir:str, file_name)-> None:
    data: list = []

    get_info(dir, data)

    write_json(file_name, data)

    write_csv(file_name, data)
    
    write_pickle(file_name, data)
    

def write_json(file_name: str, res:list[dict])-> None:
    with open(f'{file_name}.json', 'w') as f_wr:
        json.dump(res, f_wr, indent=4)


def write_csv(file_name: str, res:list[dict])->None:
    with open(f'{file_name}.csv', 'w', newline='') as f_wr:
        csv_write = csv.DictWriter(f_wr, fieldnames=['name',
        'type', 'size', 'files', 'parent'])
        csv_write.writeheader()
        csv_write.writerows(res)


def write_pickle(file_name: str, res:list[dict])->None:
    with open(f'{file_name}.pickle', 'wb') as f_wr:
        pickle.dump(res, f_wr)        


if __name__ == "__main__":
    write_info('E:\GB\Pyton_Data\Homework_8', 'info_dir')
