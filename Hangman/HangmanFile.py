# source objects
from randomWords import WordGenerator
from ASCII_ART import USER_LOOSE
from replit import clear

# define class
class HangmanGame(WordGenerator):

    # define attributes
    def __init__(self, lives):
        super().__init__()
        self.LIVES = lives
        self.validatorEmptyList = '[ _ ]'

    # define methods
    def letterNotInChosenWord(self, userInput):
        if userInput not in self.randomWord:
            self.LIVES -= 1
            print(f'\n THE LETTER [ {userInput} ] IS NOT WITHIN THE WORD.')

    def letterIsOnChosenWord(self, userInput):
        for item in range(0, len(self.randomWord)):
            if self.randomWord[item] == userInput:
                self.emptyList[item] = f'[ {userInput} ]'

    def gameOverNoLives(self):
        clear()
        print(f' {USER_LOOSE} \n')
        print(f' GAME OVER. YOU HAVE RUN OUT OF LIVES. CHOSEN WORD WAS [ {self.randomWord} ]\n')











