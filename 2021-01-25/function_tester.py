

# 4 parameters
# 2 types of parameters: positional and keyword
# def abc(num1, num2, num3, num4=789, num5=45):
#     return [num1, num2, num3, num4, num5]
#
# # 1 argument
# print(abc(123, 32, num5=99, num4=56))



# # global
# day = 'Mon'
#
# def xyz(day):
#     # local
#     # day = 'Tue'
#     print(day)
#
# xyz(day)
# print(day)

def adder(*args):
    print(args)
    total = 0
    for i in args:
        total += i
    return total
    # return a + b + c

# print(adder(3, 5, 7, 9, 3, 8, a=1, b=4, c=7))
# print('hello', 'there', 'you', 'what', 123)

def get_ave(*args):
    total = 0
    for i in args:
        total += i
    return total / len(args)

print(get_ave(3, 6, 8, 10, 34, 23, 8))

