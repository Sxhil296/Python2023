# try:
#     numerator = 10
#     denominator = 0
#
#     result = numerator/denominator
#
#     print(result)
# except:
#     print("Error: Denominator cannot be 0.")





# try:
#     even_numbers = [2,4,6,8,10]
#     print(even_numbers[5])
#
# except ZeroDivisionError:
#     print('Denominator cannot be 0.')
#
# except IndexError:
#     print("Index Out Of Bound.")


# try:
#     num = int(input("Enter a number: "))
#     assert num % 2 == 0
# except:
#     print("Not an even number!")
# else:
#     reciprocal = 1/num
#     print(reciprocal)


try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

finally:
    print("finally block")
