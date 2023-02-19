# import
from ASCII import blackJackLogo
from DealingCards import DealingCards
from Scoring import Scoring
from replit import clear

# creating objects
deckManager = DealingCards()
score = Scoring()

# Creating Decks
userDeck = deckManager.fillingOutUserDeck()
computerDeck = deckManager.fillingOutComputerDeck()

# Getting Scores
userScore = score.calculatingScore(deckOfCards=userDeck)
computerScore = score.calculatingScore(deckOfCards=computerDeck)

# flag for while loop
shouldContinue = True

while shouldContinue:
    # print ASCII
    print(f' {blackJackLogo} \n')
    print(f' USER DECK: {userDeck} \n')
    print(f' COMPUTER DECK: [{computerDeck[0]}, X] \n')

    # prompt the user for a card
    addCard = input(
        '\n WOULD YOU LIKE TO GET A CARD?. TYPE [ Y ] TO CONFIRM. TYPE [ N ] TO PASS: ').upper()

    if addCard == 'Y':
        # add extra card to deck
        userDeck.append(deckManager.selectingRandCard())
        # re-calculate score
        userScore = score.calculatingScore(deckOfCards=userDeck)

    else:
        shouldContinue = False

    # while loop for computer
    while computerScore < 17:
        # add extra card to deck
        computerDeck.append(deckManager.selectingRandCard())
        # re-calculate score
        computerScore = score.calculatingScore(deckOfCards=computerDeck)

    # call comparing Scores
    score.comparingResults(user=userScore, computer=computerScore)

    # play a new match
    playNewMatch = input(
        '\n WOULD YOU LIKE TO PLAY A NEW MATCH?. TYPE [ Y ] TO PLAY AGAIN. TYPE [ X ] TO EXIT THE PROGRAM: ')

    if playNewMatch == 'Y':
        shouldContinue = False
        # call recursive funct


    else:
        # clear
        clear()
        print('\n THANKS FOR PLAYING BLACK JACK. GOOD BYE .... \n')
        shouldContinue = False

