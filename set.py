student_id = {1, 2, 3, 4, 5}
print('Student ID:', student_id)
print(type(student_id))

vowels = {'a', 'e', 'i', 'o', 'u'}
print(f'Vowels : {vowels}')

mixed_set = {1, 2, "hello", (4, 5, 6)}
print(mixed_set)


# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = { }

print(type(empty_set))
print(type(empty_dictionary))

numbers = {2, 2, 3, 4, 4, 5}
print(numbers)  #{2, 3, 4, 5}

numbers.add(7)
print(numbers)


nums = {22, 33, 44, 55, 66}
nums_list = [12, 23, 34, 45, 56]
nums.update(nums_list)
print(nums)
nums.discard(66)
print(nums)


alphabets = {'a', 'b', 'a', 'a'}
print(all(alphabets))

set = {'a', 'b', 0, 'hello'}
print(all(set))

languages = ['Python', 'Java', 'JavaScript']
print(list(enumerate(languages)))

print()

grocery = ['bread', 'milk', 'butter']
for item in enumerate(grocery):
    print(item)

print()

for count, item in enumerate(grocery):
    print(count, item)

print()

for count, item in enumerate(grocery, 100):
    print(count, item)
