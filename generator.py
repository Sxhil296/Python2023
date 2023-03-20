# def my_generator(n):
#     value = 0
#
#     while value < n:
#         yield value
#         value += 1
# for value in my_generator(4):
#     print(value)


squares_gen = ( i * i for i in range(6))
for i in squares_gen:
    print(i)