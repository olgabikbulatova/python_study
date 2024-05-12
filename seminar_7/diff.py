n = int(input())
lst = []
for i in range(n):
    a = input()
    lst.append(a)
k = int(input())
lst_2 = []
for i in range(k):
    b = input()
    lst.append(b)    
lst_3 = []
for i in lst:
    count = 0
    for j in lst_2:
        if j.lower() in i.lower():
            count += 1
    if count == k:
        lst_3.append(i)
print(lst_3)