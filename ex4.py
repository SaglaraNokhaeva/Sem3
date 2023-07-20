# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3]
print(my_list)
i = 0
while i < len(my_list):
    if my_list.count(i) == 2:
        #temp = my_list[i]
        my_list.remove(i)
        my_list.remove(i)
    else:
        i += 1
print(my_list)
