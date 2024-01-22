# Добавьте в пакет, созданный на семинаре шахматный модуль. 
# Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, 
# чтобы они не били друг друга. Вам дана расстановка 8 
# ферзей на доске, определите, есть ли среди них пара бьющих 
# друг друга. Программа получает на вход восемь пар чисел, 
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи 
# не бьют друг друга верните истину, а если бьют - ложь.

# Напишите функцию в шахматный модуль. Используйте генератор 
# случайных чисел для случайной расстановки ферзей в задаче 
# выше. Проверяйте различный случайные  варианты и выведите 
# 4 успешных расстановки.

import random


NUM = 8
RES = 4


__all__ = ['get_res', 'get_data']


def get_res(data:list[(int)])->bool:
    x  = list(i[0] for i in data)
    y  = list(i[1] for i in data)
    res = True
    for i in range(NUM):
        for j in range(i + 1, NUM):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                res = False
    return res


def generate_data():
    flag = True
    while flag:  
        data_queen = [(i+1, random.randint(1, NUM)) for i in range(NUM)]  
        if get_res(data_queen):
            flag = False
    return data_queen

def get_data():
    i = 1
    while i <= RES:
        data_lst = generate_data()
        print(data_lst)
        i += 1
            

    


if __name__ == '__main__':
    print(get_res([(1, 4), (2, 2), (3, 7), (4, 3), (5, 6), (6, 8), (7, 5), (8, 1)]))
    print(get_res([(0, 5), (1, 1), (2, 7), (3, 4), (4, 6), (5, 0), (6, 2), (7, 5)]))
    #print(generate_data())
    get_data()