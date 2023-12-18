# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
num = randint(0, 1000)
print("Угадай загаданное число от 0 до 1000.")
flag = True
for i in range(10):
    number = int(input("Введите ваше число:\n"))
    if number == num:
        flag = False
        break
    elif number > num:
        print("Загаданное число меньше")
    else:
        print("Загаданное число больше")
if flag:
    print("Попытки закончились. Вы проиграли...")
else:
    print("Вы угадали! Победа!!!")
