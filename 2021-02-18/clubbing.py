
# Club system
# The right people must be able to enter
# The club can only accomodate 100 people inside


class Club:
    name = ''
    capacity = 100
    current = 0
    drinks_served = 0
    
    def __init__(self, name, capacity=100):
        self.name = name
        self.capacity = capacity
    
    def add_person(self, who):
        if self.check_capacity():
            self.current += 1
            self.give_drink(who.complementary_drinks)
            print('Enter')
        else:
            print('Cannot enter anymore. Capacity has been reached.')
        print(f'Current capacity is now: {self.current}')
        
    def check_capacity(self):
        return self.current < self.capacity
        # if self.current < self.capacity:
        #     return True
        # else:
        #     return False

    def give_drink(self, num):
        self.drinks_served += num
        
    def get_drinks_given(self):
        return self.drinks_served

class Patrons:
    instant_entry = False
    partner = 1
    complementary_drinks = 3

class Vip(Patrons):
    instant_entry = True
    partner = 10
    complementary_drinks = 5

class Media(Patrons):
    instant_entry = True
    partner = 0
    complementary_drinks = 1

class Regulars(Patrons):
    partner = 0
    complementary_drinks = 0

class Walkin(Patrons):
    partner = 0
    complementary_drinks = 0
    
class Owner(Patrons):
    instant_entry = True
    partner = 100
    complementary_drinks = 100
    


# Running the program

xylo = Club('Xylo', 200)

abscbn = Media()
print(f'Drinks served by xylo: {xylo.drinks_served}')
xylo.add_person(abscbn)

gma = Media()
xylo.add_person(gma)

hannah = Vip()
xylo.add_person(hannah)

jim = Regulars()
xylo.add_person(jim)

earl = Walkin()
xylo.add_person(earl)

jermaine = Owner()
xylo.add_person(jermaine)

print('----------------------------------------------------------------')
print(f'Total number of drinks given by xylo: {xylo.get_drinks_given()}')
print('----------------------------------------------------------------')
