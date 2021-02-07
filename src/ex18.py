# Names, Variables, Code, Functions

def printTwo(*args):
    arg1, arg2 = args
    print(f'arg1: {arg1},  arg2: {arg2}')

    #ok, the *args is actually pointless. We can just do this.
def printTwoAgain(arg1,arg2):
    print(f'arg1: {arg1}, arg2: {arg2}')

def printOne(arg1):
    print(f'arg1: {arg1}')


def printNone():
    print("I got nothin.")

printTwo('Jeff',  'Martin')
printTwoAgain('Jefe', 'Martian')
printOne('A. single. sentence.')
printNone()