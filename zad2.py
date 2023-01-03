# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list1 = [1, 2, 3, 4, 5, 6]
list2 = list1.copy()
list3 = []
list2.reverse()
print(list1)

for i in range(len(list1)):
    if list1[i] != list2[i]:
        list3.append(list1[i]*list2[i])


temp = []
for x in list3:
    if x not in temp:
        temp.append(x)
list3 = temp
print(list3)


