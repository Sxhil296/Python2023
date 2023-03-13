import os
import shutil

print(os.getcwd()) #get current directory

os.chdir('//home/sahil/PycharmProjects/pyShop')
print(os.getcwd())
os.chdir('//home/sahil/PycharmProjects/python2023')
print(os.getcwd())
print(os.listdir())  #list all the files and subdirectories

# os.mkdir('test')
# os.rename('test', 'mydir')
# os.rmdir('mydir')

# os.mkdir('new_dir')
os.chdir('/home/sahil/PycharmProjects/python2023/new_dir')
print(os.getcwd())
file = open("test3.txt", 'w')
file.write("hello, world!")
shutil.rmtree('new_dir') #deletes a non empty directory


