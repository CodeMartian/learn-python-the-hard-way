# Reading Files

from sys import argv

script, filename = argv

filepath = '../resources/data/'
txt = open(filepath + filename)

print(f'Here\'s your file {filename}:')
print(txt.read())

print('Type the filename again:')
file_again = input('> ')

txt_again = open(filepath + file_again)

print(txt_again.read())