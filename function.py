def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')
print()

#with argumensts
def add_numbers(x, y):
    sum = x + y
    print(f'Sum : {sum}')
add_numbers(4, 5) #function call with arguments



print()

#function defination
def find_sqaure(num):
    square = num*num
    return square

square = find_sqaure(6)
print(f'Sqaure : {square}')


