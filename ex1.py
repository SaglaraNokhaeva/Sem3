# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

# Решение 1
# my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# my_set = set (my_list)
# print(*my_list)
# print(*my_set)

# Решение 2
my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
new_list = [1]
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(*my_list)
print(*new_list)