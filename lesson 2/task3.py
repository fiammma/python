# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.


word_str = input("Введите нескольких слов, разделённых пробелами: ")
word_number = 1
for i in range(word_str.count(' ') + 1):
    words = word_str.split()
    if len(str(words)) <= 10:
        print(f'{word_number} {words [i]}')
    else:
        print(f'{word_number} {words [i] [0:10]}')
    word_number += 1
