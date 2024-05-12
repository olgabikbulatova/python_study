# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
data = [int(i) for i in input('введите число через пробел').split()]
d = {}
for i in data:
    if i not in d:
        d[i] = 0
    d[i] += 1
print(len(d.keys()))