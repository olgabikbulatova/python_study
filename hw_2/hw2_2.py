# два натуральных числа X и Y (X,Y≤1000), 
# Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

s = int(input('введите сумму x и y '))
p = int(input('введите произведение x и y '))
x = 1
while x < s:
    y = s - x
    if x * y == p and x <= 1000 and y <=1000:
        print(x, y, sep=(' ,'))
        break
    x +=1