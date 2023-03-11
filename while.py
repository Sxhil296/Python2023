i = 0
n = 5
while i <= n:
    print(i)
    i += 1


print()

# program to calculate the sum of numbers until the user enters zero
# total = 0
# number = int(input("Enter a number: "))
# while number != 0:
#     total += number
#     number = int(input("Enter a number: "))
# print(f'Total: {total}')


print()

#while-else
counter = 0
while counter < 3:
    print("Inside loop")
    counter +=1
else:
    print('Inside else')


print()
#while-break-else
counter2 = 0
while counter2 <3:
    if counter2 == 1:
        break
    print("Inside loop")
    counter2 += 1
else:
    print("Inside else")