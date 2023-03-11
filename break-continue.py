for item in range(1, 6):
    if item == 3:
      break
    print(item)
print("the end")

print()


i =1
while i <= 15:
    print(f'6 * {i} = ', 6 * (i))

    if i >= 10:
        break
    i += 1

print()
for n in range(5):
    if n == 3:
        continue
    print(n)



print()
num = 0
while num < 10:
    num += 1
    if(num % 2) == 0:
        continue
    print(num)