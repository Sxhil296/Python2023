from itertools import count

infinite_iterator = count()

for i in range(10):
    print(next(infinite_iterator), end=', ')