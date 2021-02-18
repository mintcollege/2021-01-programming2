
class Character:
    arms = 2
    feet = 2
    name = ''
    
    def walk(self):
        print('I am walking!')

class Barbarian(Character):
    def break_door(self):
        print('Barbarian breaks the door.')

class Human(Character):
    def run_fast(self):
        print('Human is running really fast')

class Elf(Character):
    def talk_to_trees(self):
        print('Elf is talking to a tree')


# hannah = Elf()
# earl = Human()
# earl.walk()
# jim = Barbarian()

class Logistics:
    has_car = True

class Alive:
    breathing = True

class Alien(Alive):
    eyes = 3

class HumanBeing(Alive):
    eyes = 2

class Filipino(HumanBeing):
    language = 'Tagalog'

class Driver(Alien, Logistics):
    pass

class Employee(Filipino):
    salary = 0
    benefits = ['health', 'dental']
    parking = True
    
    def enter_office(self):
        print('I have access to enter the office')


class Intern(Employee):
    benefits = []
    parking = False

class Founder(Employee):
    salary = 90_000

class Manager(Employee):
    salary = 50_000
    parking = False
    
    def enter_office(self):
        print('I have control of the office')



    
mark = Intern()
# print(mark.breathing)
# mark.enter_office()
sally = Manager()
# sally.enter_office()
jose = Driver()
print(jose.eyes)
print(jose.has_car)
