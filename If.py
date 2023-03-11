#num = 10
num = 4
if num > 5:
    print(f'{num} is greater than 5.')

print('This statement is always executed.')

print()

#if...else
number = 10
if number > 8:
    print(f'{number} is greater than 8.')
else:
    print(f'{number} is less than 8.')

print('This statement is always executed.')

print()

#if..elif..else
number2 = 0
if number2 > 0:
    print(f'{number2} is a positive number.')
elif number2 == 0:
    print(f'{number2} is Zero')
else:
    print(f'{number2} is a negative number.')
print('This statement is always executed.')

print()

#nested if
num2 = 5
if (num2 >= 0):
    if num2 == 0:
        print('Number is 0.')
    else:
        print("Number is positive.")
else:
    print("Number is negative.")