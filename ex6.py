# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

words = input("Введите строку: ").split()
print(words)
max_len = len(max(words, key = len))
for i in range(len(sorted(words))):
    print(f"{i+1}.{sorted(words)[i].rjust(max_len+1)}")

    # или
    #print(f"{i + 1}.{sorted(words)[i]:!>{max_len+1}}")
