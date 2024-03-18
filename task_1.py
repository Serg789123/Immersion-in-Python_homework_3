# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

data = [42, 73, 5, 42, 42, 2, 2, 3, 7, 73, 42]
res1 = []

for i in data:
    n = 0
    for j in data:
        if i == j:
            n += 1
    if n > 1:
        res1.append(i)

print(list(set(res1)))


res2 = []
for i in data:
    if data.count(i) > 1:
        res2.append(i)

print(list(set(res2)))




