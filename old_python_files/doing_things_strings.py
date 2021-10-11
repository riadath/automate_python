ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("The ten things are: ", end=' ')
print(ten_things, '\n')
print("Wait there are not 10 things in that list. Let's \
fix that\n")

ten_things = ten_things.split(' ')
print(ten_things)
more_stuff = ["Day", "Night", "Songs", "Frisbee", "Corn", \
              "banana", "Girl", "Boy"]

while len(ten_things) != 10:
    next_one = more_stuff.pop()
    # print(f"Adding {next_one}")
    ten_things.append(next_one)
    # print(f"Numer of items:{len(ten_things)}")

print(ten_things, ">>Okay now?")
# print(ten_things[0])
# print(ten_things[7])

print(ten_things.pop(-7))
print('#'.join(ten_things[0:5]))

print('JOINING>>', ten_things)
ten_things = sorted(ten_things)
print(ten_things)
