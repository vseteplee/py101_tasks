"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.

Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше

Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.

Тебе может понадобится модуль random, цикл while и ветвления
"""
import random
less_border = 0
greater_border = 1000000
num = random.randint(less_border,greater_border)
print('Hi! Try to guess the Number in my mind!\n')
answer = None
while (answer != num):
    answer = input()
    if (answer == "exit") or (answer == ""): exit(0)
    if (answer.isnumeric()):
        answer = int(answer)
        if (less_border > answer) or ( answer > greater_border):
            print ("Out of borders\n")
            continue
    else:
        print ("Not a number\n")
        continue
    if answer < num:
        print('try a greater number\n')
    elif answer > num:
        print('try a less number\n')
print(r"Hooray! U R goddamn right (:")       