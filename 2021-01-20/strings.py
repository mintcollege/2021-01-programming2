# print('testing')
# DATA TYPES IN PYTHON
name = 'jen'        # str
age = 19            # int
total = 24.99       # float
female = True       # bool
grades = [88, 89, 95]   # list
total_cost = (75.00, 99.50) # tuple
userdata = {
    'username': 'jennthehen',
    'password': 'pass123',
    'access_code': 456
}   # dict

# print(userdata)
# casting
message1 = 'Hello, my name is ' + name + ' I am ' + str(age) + ' years old.'
print(message1)

message2 = 'Hello, my name is {} I am {} years old.'.format(name, age)
print(message2)

# f string
message3 = f'Hello, my name is {name} I am {age} years old.'
print(message3)

# message4 = 'Hello, my name is %s I am %s years old.' % (name, age)
# print(message4)

