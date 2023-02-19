# import
from replit import clear

# class
class Scoring:

    # attributes
    def __init__(self):
        self.score = 0

    # methods
    def calculatingScore(self, deckOfCards):

        # to catch blackjack
        if len(deckOfCards) == 2 and sum(deckOfCards) == 21:
            return self.score

        # to switch As
        elif 11 in deckOfCards and sum(deckOfCards) > 21:
            deckOfCards.remove(11)
            deckOfCards.append(1)

        self.score = sum(deckOfCards)

        return self.score

    # comparing results
    def comparingResults(self, user, computer):

        # clear
        clear()

        if user == computer:
            print(f'\n IT IS A DRAW. COMPUTER SCORE: [ {computer} ] || USER SCORE: [ {user} ] \n')

        elif computer == 0:
            print(f'\n COMPUTER HAS A BLACK JACK. COMPUTER WINS! || COMPUTER SCORE: [ {computer} ] \n')

        elif user == 0:
            print(f'\n USER HAS A BLACK JACK. USER WINS! || USER SCORE: [ {user} ] \n')

        elif computer > 21:
            print(f'\n COMPUTER HAS LOST. SCORE [{computer}] || USER WINS! \n')

        elif user > 21:
            print(f'\n USER HAS LOST. SCORE [{user}] || COMPUTER WINS! \n')

        elif computer > user:
            print(f'\n COMPUTER WINS!. COMPUTER SCORE: [ {computer} ] || USER SCORE: [ {user} ] \n')

        else:
            print(f'\n USER WINS!. USER SCORE: [ {user} ] || COMPUTER SCORE: [ {computer} ] \n')

