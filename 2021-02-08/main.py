
# Here begins the football system

# fight off each team
# log the score
# generate the scoreboard


# games_played = {
#     'team1': ['team2', 'team3', 'team4'],
#     'team2': ['team1', 'team4', 'team3']
# }

def has_played(team, opponent, games_played):
    # Check if both teams have already played against each other
    if team in games_played[opponent] or opponent in games_played[team]:
        return True
    return False

def get_team_list():
    # sol'n 1:
    teams = input('Which teams are playing? ')  # team1, team2, team3, team4, team5
    team_list = teams.split(', ')
    
    # sol'n 2:
    # team_list = []
    # for i in range(3):
    #     team = input('Type a name of a team? ')
    #     team_list.append(team)
    
    return team_list

def round_robin(teams):
    # Reset the season
    scoreboard = {}
    games_played = {}
    for team in teams:
        scoreboard[team] = 0
        games_played[team] = []
    
    # Teams fight off against each other
    for team in teams:
        for opponent in teams:
            # check if both teams are on that list
            if team == opponent or has_played(team, opponent, games_played):
                continue
            # Add each team to list of played games
            games_played[team] = [*games_played[team], opponent]
            games_played[opponent] = [*games_played[opponent], team]
            
            # add scores to each team
            winner = input(f'{team} vs {opponent}? ')
            if winner == team:
                scoreboard[team] = scoreboard[team] + 3
            elif winner == opponent:
                scoreboard[opponent] = scoreboard[opponent] + 3
            elif winner == 'draw':
                scoreboard[team] = scoreboard[team] + 1
                scoreboard[opponent] = scoreboard[opponent] + 1
    return scoreboard

def round_robin2(teams):
    # Alternative to round_robin()
    scoreboard = {}
    games_played = {}
    for team in teams:
        scoreboard[team] = 0
        games_played[team] = []

    # Teams fight off against each other
    for team in teams:
        for opponent in teams:
            winner = ''
            valid_team = False
            
            # check if both teams are on that list, if yes then skip
            if team == opponent or has_played(team, opponent, games_played):
                continue
            
            # loop until they choose a right team or draw
            while not valid_team:
                winner = input(f'{team} vs {opponent}? ')
                if winner in [team, opponent, 'draw']:
                    valid_team = True
                else:
                    print(f'Choose: {team}, {opponent}, or draw: ')
                    
            # Add each team to list of played games
            games_played[team].append(opponent)
            games_played[opponent].append(team)
            
            # add scores to each team
            if winner == team:
                scoreboard[team] += 3
            elif winner == opponent:
                scoreboard[opponent] += 3
            elif winner == 'draw':
                scoreboard[team] += 1
                scoreboard[opponent] += 1
    return scoreboard


def create_table(score):
    # Creates the table to be printed on the screen
    table = f'\nAnd the winners are:\n'
    table += f'{"-" * 27}\n'
    for team, pts in score.items():
        table += f' {team:<20}| {pts:<2} |\n'
    table += f'{"-" * 27}\n'
    return table

# ask user for the teams
teams = get_team_list()
scoreboard = round_robin2(teams)
display_table = create_table(scoreboard)
print(display_table)

