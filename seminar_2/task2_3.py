# Пользователь вводит N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50 сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов

data = [int(i) for i in input('введите число через пробел ').split()]
n = len(data)
if n > 100:
    exit()
max = 0
count = 0
for i in data:
    if i > 0:
        count += 1
        if max < count:
            max = count  
    else:
        count = 0      
print(max)