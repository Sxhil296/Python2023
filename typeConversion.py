#implicit type conversion

int_num = 3
float_num = 3.4
new_num = int_num+float_num
print('Value:', new_num)
print('Data Type:', type(new_num))

print()

#explicit type conversion
num_string = '12'
num_int = 21
print(type(num_string))
num_string = int(num_string)
print(type(num_string))
new_sum = num_int + num_string
print(new_sum)
print(type(new_sum))