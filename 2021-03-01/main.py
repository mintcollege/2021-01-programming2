
class NotMintEmail(Exception):
    def __init__(self):
        self.message = 'Use only a valid MINT Email.'
    
    def __str__(self):
        return self.message


class NotGmailEmail(NotMintEmail):
    def __init__(self):
        self.message = 'Use only a valid GMAIL Email.'
        

class NotAnEmail(Exception):
    pass


def arithmetic(num1, num2):
    total = 0
    try:
        # print(abc)
        if num2 == 0:
            print('Nope cannot continue with that.')
            return None
        
        total = num1/num2
        
        # try:
        #     pass
        # except:
        #     pass
        
    except ZeroDivisionError:
        print('You cannot divide by 0 or the world will end.')
    except TypeError:
        print('Only input valid integers please.')
    except NameError:
        print('Do not use that variable bro.')
    except Exception as e:
        print(e)
        # print('Caught the error. But I do not know what type.')
        
    try:
        pass
    except Exception as e:
        print(e)
    
    print('The program is fine.')
    return total

# total = arithmetic(22, 0)
# print(total)




def getname():
    name = input('What is your name: ')
    if name == '2':
        raise TypeError('You cannot use the no. 2')
    return name

def create_sentence(name_of_person):
    sentence = 'Your name is ' + name_of_person + '.'
    print(sentence)

# try:
#     create_sentence(getname())
# except TypeError:
#     print('Something happened.')


def a():
    # if
    # elif
    raise NotMintEmail('Something was bad.')
    print('A is called')

def b():
    print('B is called')
    a()

def c():
    print('C is called')
    b()
    
def d():
    print('D was called')
    try:
        c()
    except NotMintEmail as e:
        print(e.message)
        print('There was as a problem.')
    
d()



