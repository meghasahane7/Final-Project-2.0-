class Team:
    def __init__(self, name):
        self.name = name
        self.points = 0

teams = [
    Team("India"),
    Team("Australia"),
    Team("England"),
    Team("New Zealand"),
    Team("South Africa")
]

# Simulating some match results
results = [
    ("India", "Australia", "win"),  # India wins against Australia
    ("England", "New Zealand", "win"),  # England wins against New Zealand
    ("South Africa", "India", "win"),  # South Africa wins against India
    ("Australia", "England", "loss"),  # Australia loses against England
    ("New Zealand", "South Africa", "loss")  # New Zealand loses against South Africa
]

# Updating team points based on match results
for team1, team2, result in results:
    if result == "win":
        for team in teams:
            if team.name == team1:
                team.points += 2
            elif team.name == team2:
                team.points += 1
    elif result == "loss":
        for team in teams:
            if team.name == team1:
                team.points += 1
            elif team.name == team2:
                team.points += 2

# Sorting teams based on points
teams.sort(key=lambda x: x.points, reverse=True)

# Displaying the ranking table
print("ICC Ranking Table:")
print("{:<10} {:<10}".format("Team", "Points"))
print("-" * 20)
for i, team in enumerate(teams, start=1):
    print("{:<10} {:<10}".format(f"{i}. {team.name}", team.points))
