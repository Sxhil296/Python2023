string1 = "Python programming"
print(string1)
print(len(string1))
print(string1[5])
print(string1[3:8])
print('z' in string1)
print('z' not in string1)
print(string1.upper())
print(string1.lower())
print(string1.capitalize())
print(string1.partition(' '))
for letter in string1:
    print(letter)

# multiline string
message = """
Never gonna give you up
Never gonna let you down
"""
print(message)

text = "bat ball"
print(text)
print(text.replace('ba', 'ro'))

message2 = 'Python is a fun programming language'
# check the index of 'fun'
print(message2.find('fun'))


sentence = "Do small things with great love"
print(len(sentence))
print(sentence.find('love'))
print(sentence.find('love', 10, 40))
print(sentence.find('love', 28, 31))
print(sentence.find('small', 2))
print(sentence.find('all', 2))

name = "Shahrukh Khan"
country = "India"
print(f'{name} is from {country}.')