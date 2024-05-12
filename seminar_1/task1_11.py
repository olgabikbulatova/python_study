# Посчитайте сумму чётных элементов от 1 до n исключая кратные e. 
# Используйте while и if. 
# Попробуйте разные значения e и n.

e = 3
n = 20
summ = 0
i = 1
while i<= n:
    if i % e == 0:
        i += 1
        continue
    if i % 2 == 0:
        summ += i
        print(i)
    i += 1
print(summ)
