# import
from HangmanFile import HangmanGame
from ASCII_ART import GAME_EXIT, LOGO_GAME, STAGES, USER_WIN
from replit import clear

# HANGMAN FUNCTION GAME
def hangmanFunctionGame():
    # Initiate the Game
    print(f' {LOGO_GAME} \n')

    print('\n TRY TO GUESS THE WORD.')

    # Constants
    LIVES = 6

    # Initiate object
    hangman = HangmanGame(lives=LIVES)

    # print list
    clueList = hangman.creatingEmptyList()

    # while loop flag
    shouldContinue = True

    while shouldContinue:

        # print lives
        print(f'\n LIVES: [ {hangman.LIVES} ]')

        # print list
        print(f'\n {clueList}')

        # print ASCII
        print(f'\n {STAGES[hangman.LIVES]}')

        print(hangman.randomWord)

        # user input
        userInputText = input('\n ENTER A LETTER FROM (A - Z) ONLY: ').lower()

        # clear
        clear()

        # validations
        # letter not in word
        hangman.letterNotInChosenWord(userInput=userInputText)

        # if lives = 0
        if hangman.LIVES == 0:
            shouldContinue = False
            hangman.gameOverNoLives()

        # letter in word
        hangman.letterIsOnChosenWord(userInput=userInputText)

        # validate if user wins
        if '[ _ ]' not in clueList:
            clear()
            shouldContinue = False
            print(f' {USER_WIN} \n')
            print(f' YOU WIN!. THE GUESSING WORD WAS: [ {hangman.randomWord} ]\n')

        # play again ?
        playAgain = input(' WOULD YOU LIKE TO PLAY AGAIN?. TYPE [ Y ] TO PLAY. TYPE [ X ] TO EXIT: ').upper()
        if playAgain == 'Y':
            # clear
            clear()
            # recursive function
            hangmanFunctionGame()

        else:
            # clear
            clear()
            shouldContinue = False
            print(f' {GAME_EXIT} \n')
            print(' THANK YOU FOR PLAYING. GOOD BYE ..... \n')

# call the funct
hangmanFunctionGame()













