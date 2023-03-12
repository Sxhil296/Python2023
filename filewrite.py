with open("test2.txt", "w") as file2:
    file2.write("Python is cool.")
    file2.write("\nProgramming with Python is fun.")
    print(file2.writable())

with open("test2.txt", "r") as file2:
    print(file2.read())
    print(file2.fileno())
    print(file2.readable())
    print(file2.writable())