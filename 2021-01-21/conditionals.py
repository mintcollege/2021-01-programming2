
# age = 17
user = {
    'age': 17,
    'username': 'lilypichu',
    'vip': True,
    'is_male': False
}
user = dict(age=17, username='lilypichu', vip=True, is_male=False)


if user['age'] >= 18 and user['age'] <= 50:
    print('Enter.')
elif user['age'] >= 100:
    print('You can also enter')
elif user['vip']:
    print('You can enter because you are vip')
elif not user['is_male']:
    print('You can enter')
# else:
#     print('You cannot enter.')

print('This is after the conditional')

# Types of conditions
# ==
# !=
# > >=
# < <=
# age > 17 and user['is_female']
# age > 17 or user['is_female']
# user['vip']
# not user['vip']
# a is None
# a is not None

a = None
user = None
name = ''
userlist = []
userdata1 = {}
userdata2 = dict()
age = None



# Fibonacci sequence
# 1, 1, 2, 3, 5, 8, 13, 21, ...