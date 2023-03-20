#nested function
# def greet(name):
#     def display_name():
#         print(f'Hii, {name} !')
#     display_name()
# greet("John")

def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func

odd = calculate()
print(odd())
odd2 = calculate()
print(odd2())