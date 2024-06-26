# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не превосходящее 105
# Программа должна вывести все пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую пару не дает).

def find_friend(n):
    res = 0
    res_1 = 0
    for i in range(1, n):
        if n % i == 0:
            res += i
    for i in range(1, res):
        if res % i == 0:
            res_1 += i
    if res_1 == n and n != res:
        return n, res      


k = int(input("введите число: "))
r = []
for i in range(1, k-1):
    a = find_friend(i)
    if a:
        if a[::-1] not in r:
            r.append(a)
for i in r:
    print(*i)
  
