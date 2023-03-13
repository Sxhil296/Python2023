# class Parrot:
#     #class attribute
#     name = ""
#     age = 0
#
# #create parrot1 object
# parrot1 = Parrot()
# parrot1.name = "Blu"
# parrot1.age = 2
#
# #create another object parrot2
# parrot2 = Parrot()
# parrot2.name = "Woo"
# parrot2.age = 4
#
# #access attributes
# print(f'{parrot1.name} is {parrot1.age} years old.')
# print(f'{parrot2.name} is {parrot2.age} years old.')


# define a class
class Bike:
    name = ""
    gear = 0

# create object of class
bike1 = Bike()

# access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")





class Employee:
    employee_name = ""
    employee_id = 0

employee1 = Employee()
employee2 = Employee()

employee1.employee_id = 1001
employee1.employee_name = "Ritik"
employee2.employee_id = 1002
employee2.employee_name = "Vivek"
print(f'{employee1.employee_name} has id {employee1.employee_id}.')
