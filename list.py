list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list)
print(list[0:5])
print(list[5:])
print(list[:9])
print(list[:])


list.append(10)
print(list)

list2=[12, 23]
list.extend(list2)
print(list)

list.insert(0, 'a')
print(list)

list.remove(2)
print(list)
list.pop(0)
print(list)
