

class Team:
    # class attributes
    name = ''
    games = 0
    abc = 'foobar'
    
    def __init__(self, name, *, games=12, colors='red', members=10, country='US',
                 has_coach=True, years_active=32):
        # object attributes
        self.name = name
        self.games = games
        self.colors = colors
        self.members = members
        self.country = country
        self.has_coach = has_coach
        self.years_active = years_active


team1 = Team('Bulls', games=12, colors='red', members=10, country='US',
             has_coach=True, years_active=12)
print(team1.name)
print(team1.years_active)
print(team1.country)

# team2 = Team('Hornets', 7)
# # team2.name = 'Hornets'
# # team2.games = 7
# print(team2.name)
# print(team2.games)
# print(team2.abc)