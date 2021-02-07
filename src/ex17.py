# More files

from sys import argv
from os.path import exists

script, fromFile, toFile = argv
filePath = '../resources/data/'

print(f'Copying from {fromFile} to {toFile}')

with open(filePath + fromFile, 'r') as inFile:
    inData = inFile.read()

    print(f'The input file is {len(inData)} bymes long.')

    print(f'Does the output file exist? {exists(toFile)}')

    input('Press Enter to Continue. CTRL-C (^C) to abort.')

with open(filePath + toFile, 'w') as outFile:
    outFile.write(inData)

