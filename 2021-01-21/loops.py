

nums = [2, 6, 3, 9]

counter = 0
for i in nums:
    # print(counter, i, type(i))
    # counter = counter + 1
    counter += 1
    # part of the loop


# sum = 0
# for idx, val in enumerate(nums):
#     # print(idx, val, type(val))
#     sum += val
#
# print('Average is:', sum // len(nums))

# iterators
name = 'Jose Rizal'
for idx, val in enumerate(range(1_000)):
    # print('hello')
    pass

for i in []:
    pass

# code here


# pseudo code
# ask user for a number
# add that number to a list
# when the user types 'exit' the program will get the average


# Ask the user an infinite number of times until they exit
total = 0
counter = 0
while True:
    inp = input('Type a number: ')
    if inp == 'exit':
        ave = total / counter
        print('Average is:', ave)
        break
    total += int(inp)
    counter += 1

