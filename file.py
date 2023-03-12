# open a file
file1 = open("test.txt", "r")
# read the file
read_content = file1.read()
print(read_content)
# close the file
file1.close()




#If an exception occurs when we are performing some operation with the file,
# the code exits without closing the file.
#A safer way is to use a try...finally block.
try:
    file1 = open("test.txt", "r")
    read_content = file1.read()
    print(read_content)
finally:
    # close the file
    file1.close()





#we can use the with...open syntax to automatically close the file
with open("test.txt", "r") as file1:
    read_content = file1.read()
    print(read_content)