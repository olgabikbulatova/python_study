# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def change_mark(x):
    for i in range(len(x)):
        if x[i] == max(x):
            x[i] = min(x)
    print(*x)


grade = [int(i) for i in input('введите числа через пробел ').split()]
# print(*grade)
# for i in range(len(grade)):
#     if grade[i] == max(grade):
#         grade[i] = min(grade)
# print(*grade)
change_mark(grade)
