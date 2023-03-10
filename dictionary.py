# create a dictionary named capital_city
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}
print(capital_city)
print(capital_city['Nepal'])
print(capital_city.keys())
print(capital_city.values())
print(capital_city.clear())
print()

print(sorted(capital_city))
numbers = {1: 'One', 2: 'Two', 3: 'Three'}
print(numbers[3])
numbers[4] = 'Four'
print(numbers)
numbers[3] = 'teen'
print(numbers)
print(numbers[4])
del numbers[3] #deletes three
print(numbers)
print(len(numbers))

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])


