# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

data = [int(i) for i in input('введите число через пробел ').split()]
count_x = 0
count_y = 0
for i in data:
    if i == 0:
        count_x += 1
    else:
        count_y += 1
if count_x > count_y:
    print(count_y)
else:
    print(count_x)
               