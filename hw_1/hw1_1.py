# Нарисовать в консоли ёлку спросив 
# у пользователя количество рядов. 
# Пример результата:
# Сколько рядов у ёлки? 5
a = int(input())
i = 1
x = '*'
while i<=a:
    print(x.center(a*2-1))
    x = x + '**'
    i +=1
