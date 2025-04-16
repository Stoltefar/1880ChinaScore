# Main app that will create a game asking how many players are in it and create objects of Player, MajorCompanies classes.

print("How many players are in this game?")
PLAYER_COUNT = int(input())

print("Number of players: " + (str(PLAYER_COUNT)))

# TODO Let user add Players in any order. 
# TODO Create setup share round method to handle auctioning of Private Companies and the resulting player expenses and stock gains.
# TODO Sort player order after remaining cash.
class Player:
    """A container for keeping track of the holdings for each player."""

    # TODO Add Portfolio to the Player class
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

print("\nPerform setup Share round by auctioning out the Private Companies P0 - P7.")
print("In order of remaining cash, starting from the bottom, enter Player info.")

playerList = []

for i in range(PLAYER_COUNT):
    print("Enter name of player " + str(i+1))
    playerName = input()
    print("Enter amount of cash " + playerName + " has left.")
    playerWallet = int(input())
    newPlayer = Player(playerName, playerWallet)
    playerList.append(newPlayer)

print(playerList[0].name)
