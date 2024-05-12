# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# def same_by(characteristic,objects):
#     if not objects:
#         return True
#     first = characteristic(objects[0])
#     for i in objects:
#         if characteristic(i) != first:
#             return False
#     return True

def same_by(characteristic,objects):
    if not objects:
        return True
    data = list(map(characteristic, objects))
    if max(data) == min(data):
        return True


values = [30, 2, 10, 6]
if same_by (lambda x: x % 2, values):
    print('same')
else:
    print('different')
