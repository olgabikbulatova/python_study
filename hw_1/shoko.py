n = int(input('длина шоколадки долек '))
m = int(input('ширина шоколадки долек '))
k = int(input('сколько долек отломить? '))

if n*m>k and k%n==0 or k%m == 0:
    print('yes')
else: print('no')