# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.

# Функция не должна ничего выводить, только возвращать значение.



def f(x, y):
    if y == 0:
        return 1
    return x * f(x, y-1)


a = 3
b = -1
print(f(a, b))