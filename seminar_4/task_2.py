# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.


a = set(input('введите фразу: ').lower().split())
# print(len(a))
# word = set()
# for i in a:
#     word.add(f'{i}')
print(len(a))