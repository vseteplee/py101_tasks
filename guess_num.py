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