# import
from random import choice
from replit import clear

# constants
DECK_OF_CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# class
class DealingCards:

    # attributes
    def __init__(self):
        self.userDeck = []
        self.computerDeck = []

    # methods
    def selectingRandCard(self):
        randomCard = choice(DECK_OF_CARDS)
        return randomCard

    # decks
    def fillingOutUserDeck(self):
        for item in range(1, 3):
            self.userDeck.append(self.selectingRandCard())

        return self.userDeck

    def fillingOutComputerDeck(self):
        for item in range(1, 3):
            self.computerDeck.append(self.selectingRandCard())

        return self.computerDeck


