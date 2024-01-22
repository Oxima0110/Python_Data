# ✔ Напишите функцию, которая открывает на чтение созданные 
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните 
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя 
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя 
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, 
# сколько в более длинном файле. 
# ✔ При достижении конца более короткого файла, 
# возвращайтесь в его начало.


__all__ = ['num_name']

def get_line(name:str)->str:
    line = name.readline()
    if not line:
        name.seek(0)
        return get_line(name)
    return line[:-1]

    
def num_name(name_num:str, name_name:str, name_res:str)-> None:
    with (open(name_num, 'r', encoding='utf-8') as f_num,
          open(name_name, 'r', encoding='utf-8') as f_name,
          open(name_res, 'w', encoding='utf-8') as f_res
          ):
        max_len = max(sum(1 for _ in f_num), sum(1 for _ in f_name))
        for _ in range(max_len):
            num = get_line(f_num)
            name = get_line(f_name)
            num_1, num_2 = num.split('|')
            mult = int(num_1) * float(num_2)
            if mult < 0:
                f_res.write(f'{name.lower()} {abs(mult)}\n')
            else:
                f_res.write(f'{name.upper()} {round(mult)}\n')


if __name__ == '__main__':   
    print(num_name('task1.txt', 'task2.txt', 'task3.txt'))