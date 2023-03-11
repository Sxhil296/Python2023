import math
sqaure_root = math.sqrt(4)
print(f'sqaure root of 4 is: {sqaure_root}')
print()



power = pow(2,3)
print(f'2 to the power 3 : {power}')
print()



def get_sqaure(num):
    return num * num
for i in [1,2, 3]:
    result = get_sqaure(i)
    print(f'Sqaure of {i} = {result}')