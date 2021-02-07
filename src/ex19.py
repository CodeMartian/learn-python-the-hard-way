# Functions and Variables

def cheeseAndCrackers(cheeseCount, boxesOfCrackers):
    print(f'You have {cheeseCount} cheeses!')
    print(f'You have {boxesOfCrackers} boxes of crackers!')
    print('Man, that\'s enough for a party!')
    print('Get a blanket.\n')

print('We can just give the function numbers directly:')
cheeseAndCrackers(20, 30)

print('OR, we can use variables from our script:')
amtCheese = 10
amtCrackers = 30

cheeseAndCrackers(amtCheese, amtCrackers)

print('We can even do math inside too:')
cheeseAndCrackers(10 + 20, 5 + 6)

print('And we can combine the two, variables and math:')
cheeseAndCrackers(amtCheese + 10, amtCrackers + 1000)