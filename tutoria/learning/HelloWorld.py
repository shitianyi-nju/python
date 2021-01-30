# hello world
print("Hello world")

# calculate
x = 2
y = 3
print(x + y)

# if/elif/else
number = 23
guess = int(input('Enter an integer : '))
if guess == number :
    print("1111")
elif guess < number:
    print("2222")
else:
    print("3333")

# while
running = True
while running:
    guess = int(input("Enter an guess : "))

    if guess == number:
        running = False
    elif guess < number:
        print("guess less than number")
    else:
        print("guess more than number")
else:
    print("exit while")
print("Done")

# for
# range(i, j)  from i to j - 1
# range(i, j, step) i, i+step i + 2* step ... less than j
for i in range(1, 10):
    print(i)
else:
    print("loop over")

# break
while True:
    s = input("Enger an input : ")
    if s == "quit":
        break;
print("break")