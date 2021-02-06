typesOfPeople = 10
x = f"There are {typesOfPeople} types of people in the world."

binary = 'binary'
doNot = "don't"
y = f"Those who understand {binary}, and those who {doNot}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = False
joke_evaluation = "Isn't that joke funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side"

print(w + e)