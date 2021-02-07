from sys import argv

script, inputFile = argv
filePath = '../resources/data'

def printAll(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def printALine(lineCount, f):
    print(lineCount,  f.readline())

with open(filePath + inputFile, 'w+') as currentFile:
    print('First let\'s print the whole file. \n')

    printAll(currentFile)

    print('Now let\'s rewind, kind of like a tape.')

    rewind(currentFile)

    print('Now let\'s print three lines.\n')

    currentLine = 1
    printALine(currentLine, currentFile)
    currentLine += 1
    printALine(currentLine, currentFile)
    currentLine += 1
    printALine(currentLine, currentFile)