# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# Функция не должна ничего выводить, только возвращать значение.

def sum(a, b):
    if b == 0:
        return a 
    return sum(a + 1, b - 1)


a = 10
b = 5
print(sum(a, b))