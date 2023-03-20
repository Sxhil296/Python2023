import re

# pattern = '^a...s$'
# test_string = 'abyss'
# result = re.match(pattern, test_string)
# if result:
#     print("Search successful!")
# else:
#     print("Search unsuccessful")
#


# string = 'hello  1 2 3 hn hnn'
# pattern = '\d+'
# result = re.findall(pattern, string)
# print(result)


# string = 'Twelve:12 Eighty nine:89.'
# pattern = '\d+'
#
# result = re.split(pattern, string)
# print(result)


string = "Python is fun"

# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")
