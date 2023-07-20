# Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ — символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают или не совпадают в ваших решениях
from collections import Counter

obj = input("Введите строку: ")
res1 = {}
res2 = {}
res3 = Counter(obj)
res4 = {}

for i in obj:
    res1[i] = res1.setdefault(i, 0)+1

for i in obj:
    if i not in res2:
        res2[i] = obj.count(i)

for i in obj:
    if i not in res4:
        res4[i] = 0
    res4[i] +=1

print(res1, res2, res3, res4, sep='\n')
