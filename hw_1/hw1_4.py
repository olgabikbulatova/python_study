# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу 
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

a = int(input())
i = 2
while i <= a:
    if a % i == 0 and i == a:
        print('prime')
        break
    i += 1
else:
    print('compos')

   

