# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


f1 = 0
f2 = 1

lst = []
n = int(input('vvedi 4islo '))

for i in range(1, n):
    f1, f2 = f2, f1+f2
    # print(f2, end=' ')
    lst.append(f2)
    lst.append((-1)*f2)

lst.append(-1)
lst.append(0)
lst.append(1)
lst.sort()
print(lst)









