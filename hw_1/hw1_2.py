#Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
a = 2
b = 2
while a<=9:
    print(a, 'x', b, '=', a*b)
    b += 1
    if b > 10:
        a += 1
        b = 1
