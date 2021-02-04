
"""
Football Tally System

Ask the user for 3 teams
Those 3 teams must face each other round robin - input() save as a list
Log who is the winner/loser/draw for each game - user will type the name of the winner or "draw"
Assign points based on the game: Winner 3pts, Draw 1pt, Loss 0pts - dict()
Display a table showing the points of each team - fstring
"""

# name = 'john'
# print(f'My name is {name}.')
#
# table = '''
# Atletico Madrid     12
# Barcelona           10
# Real Madrid         4
# '''
# print(table)
# team1 = 'Atletico Madrid'
# team2 = 'Barcelona'
# team3 = 'Real Madrid'
# standings = f'''
# {team1:<20}| 12 | {team1} |
# {team2:<20}| 10 | {team2:>20} |
# {team3:<20}| 4  | {team3:>20} |
# '''
# print(standings)

# print(teams)
# Face-off of teams
def update_tally(team, points):
    pass

def ask_result(team, opponent):
    winner = input('Who is the winner? ')
    if winner == 'draw':
        # team gets a point
        # opponent gets a point
        pass
    # Something like that...

def display_tally(data):
    '''
    data = {
        'team1': score,
        'team2': score,
        'team3': score,
    }
    '''
    table = ''
    for teamname, score in data.items():
        table += f'data here\n'
    return table

final_tally = {}
teams = input('What are the 3 teams? ')
teams = teams.split(', ')

for team in teams:
    for opponent in teams:
        if opponent == team:
            # skips the rest of the code and moves on to the next loop instead
            continue
        # Here I would ask the user what happened and then make a note of it
        # Loop through the final tally
        # Write the entire code here w/o separating them into functions
        
# After all is said and done then I would print the results
table = display_tally(final_tally)
print(table)



'''
Sample code from the terminal

>>> a = {'team1': 12, 'team2': 4000, 'team3':123}
>>> a
{'team1': 12, 'team2': 4000, 'team3': 123}
>>> for i in a.items():
...     print(i)
...
('team1', 12)
('team2', 4000)
('team3', 123)
>>> username, age = ('hey', 18)
>>> print(username)
hey
>>> print(age)
18
>>> username, age = ['hey', 18]
>>> username
'hey'
>>> age
18
>>> username, age, rating, roomnum = ['hey', 18, 'aaa', 23]
>>> roomnum, username, age, rating = ['hey', 18, 'aaa', 23]
>>> roomnum
'hey'
>>> for teamname, score in a.items():
...     print(teamname, score)
...
team1 12
team2 4000
team3 123
>>> a
{'team1': 12, 'team2': 4000, 'team3': 123}
>>> a['team1']
12
>>> a['team1'] = a['team1'] + 3
>>> a
{'team1': 15, 'team2': 4000, 'team3': 123}
>>> a['team1'] = a['team1'] + 0
>>> a['team1'] = a['team1'] + 1
>>> a
{'team1': 16, 'team2': 4000, 'team3': 123}
>>> b = 1
>>> b
1
>>> b = b + 1
>>> b
2
>>> b = b + 3
>>> b
5
>>> a['team2']
4000
>>> a['team2'] = a['team2'] + 1
>>> a['team2']
4001
>>> clear
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'clear' is not defined
>>>
>>> b
5
>>> x = b + 1
>>> x
6
>>> x = b + 32
>>> x
37
>>> x = b + 34
>>> x
39
>>> x = b + 34
>>> x
39
>>> b = b + 34
>>> b
39
>>> b = b + 1
>>> b
40
>>> b = 1
>>> b
1
>>> b = b + 2
>>> b
3
>>> b = b + 2
>>> b
5
>>> b = b + 2
>>> b
7
>>> b = b + 1
>>> b
8
>>> b = b + 1
>>> b
9
>>> b += 1
>>> b
10
>>> b += 2
>>> b
12
>>> b *= 3
>>> b
36
>>> b /= 3
>>> b
12.0
>>> b
12.0
>>> b += 2
>>> b
14.0
>>> b = int(b)
>>> b
14
>>> teams['Barcelona'] = teams['Barcelona'] + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'teams' is not defined
>>> a['team1'] = a['team1'] + 3
>>> a['team1']
19
>>> a['team1'] = a['team1'] + 3
>>> a['team1']
22
>>> table = display_tally(a)
'''