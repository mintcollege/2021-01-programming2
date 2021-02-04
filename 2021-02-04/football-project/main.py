
# Football project
# Ask the user for 3 teams
# Those 3 teams must face each other round robin - input() save as a list
# Log who is the winner/loser/draw for each game - user will type the name of the winner or "draw"
# Assign points based on the game: Winner 3pts, Draw 1pt, Loss 0pts - dict()
# Display a table showing the points of each team - fstring

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

teams = input('What are the 3 teams? ')
teams = teams.split(', ')
# print(teams)
# Face of of teams
final_tally = {
    'Barcelona': {
        'win': 2,
        'loss': 1,
        'draw': 1
    },
    'Real Madrid': {},
    'Betis': {}
}