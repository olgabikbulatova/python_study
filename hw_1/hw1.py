#Найдите сумму цифр трехзначного числа.

a= input('введите трех значное число ')
print (int(a[0])+int(a[1])+int(a[2]))

# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

a = int(input('сколько всего журавликов сделали дети? '))
c = int(a/6)
k = (a-(c+c))
print('Катя сделала', k,', Петя сделал ', c, ', Сережа сделал', c)

# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
a = input('введите номер билета ')
b = int(a[0])+int(a[1])+int(a[2])
c = int(a[3])+int(a[4])+int(a[5])
if b==c:
    print('yes')
else: print('no')

# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no
n = int(input('длина шоколадки долек '))
m = int(input('ширина шоколадки долек '))
k = int(input('сколько долек отломить? '))

if n*m > k and k%n == 0 or k%m == 0:
    print('yes')
else: print('no')