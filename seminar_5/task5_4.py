# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

# def reverse(x):
#     if x == 1:
#         return 1
#     return for i in range(len(x+1)):
#         if i 

# s = input("enter numbers ")
# print(s[::-1])

def seq(s, i = None):
    if i is None:
        i = len(s)
    if i <= 0:
        return
    print(s[i-1], end = '')
    seq(s, i-1)


seq(input('enter numbers: '))
