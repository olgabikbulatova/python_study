# самый легкий и самый тяжелый арбуз? 
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

data = [int(i) for i in input('введите число через пробел ').split()]
max_a = data[0]
min_a = data[0]
for i in data:
    if i > max_a:
        max_a = i
    elif i < min_a:
        min_a = i
print(max_a, min_a)    
