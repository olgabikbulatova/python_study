# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа 
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного 
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
num = randint(0, 1000)
a = int(input('введите число '))
i = 1
while i <= 10:
    if a == num:
        print('you win!')
        break
    elif a > num:
        print('меньше')
    elif a < num:
        print('больше')
    i += 1
    print('попытка ', i)
    a = int(input('введите число еще раз '))   
else:
    print('попытки закончились') 