# Main app that will create a game asking how many players are in it and create objects of Player, MajorCompanies classes.

print("How many players are in this game?")
PLAYER_COUNT = int(input())

print("Number of players: " + (str(PLAYER_COUNT)))

# TODO Let user add Players in any order. 
# TODO Create setup share round method to handle auctioning of Private Companies and the resulting player expenses and stock gains.
# TODO Sort player order after remaining cash.

print("Perform setup Share round by auctioning out the Private Companies P0 - P7.")
print("In order of remaining cash, starting from the bottom, enter Player info.")