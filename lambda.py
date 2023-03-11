#declaration

greet = lambda : print('Hello')
greet()

print()

#Python lambda Function with an Argument
greet_user = lambda name : print('hey there,', name)
greet_user("Sahil")
print()

# Program to filter out only the odd items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 != 0) , my_list))

print(new_list)


print()


# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)

# Output: [2, 10, 8, 12, 16, 22, 6, 24]