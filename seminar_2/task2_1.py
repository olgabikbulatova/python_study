# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

n = int(input('введите целое неотрицательное число: '))
x = 1
i = 1
if i != 0:
    while i <= n:
        x = x * i
        i += 1  
    print(x)
else:
    print(int(1))             