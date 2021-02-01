import random
from limeutils import parse_str, split_fullname
# import antigravity

# 12.5
# total = input('What is your total score? ')
# total = parse_str(total)
# print(total, type(total))

# fullname = input('What is your fullname? ')
# firstlast = split_fullname(fullname)
# print(firstlast)

# mynumlist = [1, 2, -8, 0]
# maximum = max(mynumlist)
# minimum = min(mynumlist)
# print(maximum)
# print(minimum)

def practice_one(x):
    y = int(x / 2)

    for i in range(1, y + 1):
        for j in range(i):
            print('*', end = " ")
        print("\r")

    if (x % 2) == 1:
        y += 1

    for i in range(y, 0, -1):
        for j in range(i):
            print('*', end = " ")
        print("\r")
    return

def pattern(x):
    y = int(x / 2) + 1
    z = 2 * y - 2
    
    # Add a comment
    for i in range(0, y):
        for j in range(0, z):
            print(end = ' ')
        z = z - 1
        for j in range(0, i + 1):
            print('*', end = ' ')
        print(' ')
    
    z = y - 2
    
    for i in range(y, -1, -1):
        for j in range(z, 0, -1):
            print(end = ' ')
        z = z + 1
        for j in range(0, i + 1):
            print('*', end = ' ')
        print(' ')

# pattern(11)








num = random.randint(1, 12)
def keepguessing(guess):
    if guess > 0 and guess < 10:
        if guess < num:
            return "Too low"
        elif guess > num:
            return "Too high"
        else:
            return "Exactly right"
    
    else:
        return "Invalid number"

while True:
    guess = int(input("Guess the number between 1 and 9 (including 1 and 9): "))
    message = keepguessing(guess)
    print(message)
    if message == 'Exactly right':
        break

# num = input('Type a number: ')
# num = parse_str(num)
# pattern(num)
