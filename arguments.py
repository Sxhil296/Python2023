#default
def sum_num(a=3, b=4):
    sum = a + b
    print(sum)
sum_num()
print()


#keyword
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)
display_info(last_name = 'Cartman', first_name = 'Eric')

print()

#arbitory
def find_sum(*numbers):
    result = 0

    for num in numbers:
        result = result + num

    print("Sum = ", result)


# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)