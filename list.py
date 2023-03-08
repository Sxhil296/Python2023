list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#slicing
print(list)
print(list[0:5])
print(list[5:])
print(list[:9])
print(list[:])

#adding
list.append(10)
print(list)

list2=[12, 23]
list.extend(list2)
print(list)

list.insert(0, 'a')
print(list)


#deleting
list.remove(2)
print(list)

list.pop(0)
print(list)

list.clear()
print(list)

#indexing
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
index = list.index(5)
print(index)

#count
print(list.count(2))

#sorting
prime_numbers = [11, 3, 7, 5, 2]

# sorting the list in ascending order
prime_numbers.sort()

print(prime_numbers)

# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
vowels.sort(reverse=True)

# print vowels
print('Sorted list (in Descending):', vowels)



languages = ['Python', 'Swift', 'C++']

# iterating through the list
for language in languages:
    print(language)

    nums = [1, 2, 3, 4, 5, 6]
    for num in nums:
        print(num)
print(8 in nums)
print(len(nums))



numbers = [num*num for num in range(1,7)]
print(numbers)

numbers2 = [num for num in range(1,4)]
print(numbers2)