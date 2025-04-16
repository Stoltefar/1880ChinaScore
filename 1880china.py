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
class MajorCompany:
    """A container for keeping track of a Major company's stock value, share certificates and share holders (=Players).
    May also contain data for company funds and trains beyond MVP product."""

    def __init__(self, name, abreviation):
        self.name = name
        self.abreviation = abreviation
        self.shares = 10
        self.directorShares = 2
        
    def launch(self, director, parValue, directorShares):
        self.floated = False
        self.parValue = 0
        self.director = Player()
        self.stockBook = []

# Initiate Major companies

bcr = MajorCompany("Baocheng Railway", "BCR")
jha = MajorCompany("Jingha Railway", "JHA")
hkr = MajorCompany("Hukun Railway", "HKR")     




print("\nPerform setup Share round by auctioning out the Private Companies P0 - P7.")

# Create player list and populate it with Player objects
print("In order of remaining cash, starting from the bottom, enter Player info.")
playerList = []

for i in range(PLAYER_COUNT):
    print("Enter name of player " + str(i+1))
    playerName = input()
    print("Enter amount of cash " + playerName + " has left.")
    playerWallet = int(input())
    newPlayer = Player(playerName, playerWallet)
    playerList.append(newPlayer)


# print(playerList[0].name)
