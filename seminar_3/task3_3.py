# Напишите программу для печати всех уникальных
# значений в словаре. 

data =  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
s = set()
for d in data:
    for val in d.values():
        s.add(val.strip())
print(s)

# f = {}
# for d in data:
#     for val in d.values():
#         f[val.strip()] = 0


# print(*f.keys())