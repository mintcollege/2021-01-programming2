from datetime import datetime
import time


# Student has 3 grade scores
# Get the sum of all

# def sumofall(g1, g2, g3):
#     return g1 + g2 + g3
#
# # total = sumofall(9, 10, 10)
# # print(f'Your grade is: {total}.')
#
#
# class Calculator:
#     def compute(self, g1, g2, g3):
#         return g1 + g2 + g3
#
#
# total = Calculator()
# print(total.compute(1, 2, 5))

# class Student:
#     # Attributes/Properties
#     name = ''
#     age = 19
#     gender = 'female'
#     course = 'Fine Arts'
#     year = '4th yr'
#     address = '24 Edsa Ave, Philippines'
#     tuition_paid = True
#     home_num = ''
#     emergency_num = ''
#
#     # method
#     def __init__(self, age=None, name='', address=''):
#         self.age = age
#         self.name = name
#         self.address = address


# sam = Student(19, 'Sam', '23 Katipunan Ave')
# earl = Student(20, 'Earl', '45 Dolce Ave')
# mark = Student()
# # hannah = Student(age=19, name='Hannah')
# # print(earl2.age)
# # print(earl2.name)
# # print(earl2.course)
# print(f'Hello {sam.name} {sam.age} from {sam.course} you live in {sam.address}.')
# print(f'Hello {earl.name} {earl.age} from {earl.course} you live in {earl.address}.')
# print(f'Hello {mark.name} {mark.age} from {mark.course} you live in {mark.address}.')


# Grading system
# class Student:
#     name = ''
#
#     def __init__(self, name='hello'):
#         self.name = name
#
# class Grade:
#     grade1 = 23
#     grade2 = 45
#     grade3 = 77
#
#
# jim = Student('jim')
# test1 = Grade()
# print(jim.name)
# print(test1.grade1)


# class Team:
#     # name = 'abc'
#     # country = 'Spain'
#     # wins = 0
#     # games_played = 0
#     coach = 'Manuel Santos'
#
#     # method
#     def __init__(self, name, country='Spain', wins=0, games_played=0):
#         self.name = name
#         self.country = country
#         self.wins = wins
#         self.games_played = games_played
#
#     def increment_win(self, num=1):
#         # self.wins = self.wins + 1
#         self.wins += num
#
#     def increment_game(self, num=1):
#         self.games_played += num
#
#
# barcelona = Team('Barcelona', games_played=12)
# realmadrid = Team('Real Madrid', games_played=3)
# sevilla = Team('Sevilla', wins=7)
#
# print(barcelona.games_played)
# barcelona.increment_game(3)
# # barcelona.increment_game()
# # barcelona.increment_game()
# print(barcelona.games_played)
# print(realmadrid.games_played)

# print(barcelona.name, barcelona.country, barcelona.wins, barcelona.games_played)
# print(realmadrid.name, realmadrid.country, realmadrid.wins, realmadrid.games_played)
# print(sevilla.name, sevilla.country, sevilla.wins, sevilla.games_played)
# print(barcelona.wins)
# barcelona.add_win()
# print(barcelona.wins)
# barcelona.add_win()
# print(barcelona.wins)

class User:
    pass

class Payment:
    pass

class Student:
    pass

class TimeTracker:
    started = False
    def start_timing(self, start):
        if not self.started:
            self.start = start
            self.started = True
        else:
            print('You have already started!')
    
    def end_timing(self, end):
        self.end = end
        self.diff = self.compute_hours()
        self.started = False
        
    def compute_hours(self):
        diff = self.end - self.start
        return diff
    
    def get_mins(self):
        return self.diff / 60
    
    def get_hours(self):
        return self.diff / 3600
    
    def get_milliseconds(self):
        return self.get_seconds() * 1000
    
    def get_seconds(self):
        return self.diff.seconds
    
    def cancel_timing(self):
        pass


monday = TimeTracker()
monday.start_timing(datetime.now())
monday.start_timing(datetime.now())
monday.start_timing(datetime.now())
monday.start_timing(datetime.now())
monday.start_timing(datetime.now())
monday.start_timing(datetime.now())
monday.start_timing(datetime.now())
time.sleep(3)
monday.end_timing(datetime.now())
print(monday.get_mins())
print(monday.get_hours())
print(monday.get_seconds())
print(monday.get_milliseconds())
