ten_things = "Apples Oranges Crows Telephone Light Sugar"

print(ten_things)
print("Wait there's not ten things in that list. Let's fix that.")

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

stuff = ten_things.split(" ")
--
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print(f"Adding {next_one} to the list of things.")
    stuff.append(next_one)
    print(f"There are {len(stuff)} things now.")

print("There we go: ", stuff)

print("Let's do some things with the stuff now.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))