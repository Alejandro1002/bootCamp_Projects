# import
from random import choice

# constants
WORDS = [
    'womanly',
    'weigh',
    'nice',
    'nappy',
    'gather',
    'awful',
    'great',
    'imagine',
    'eatable',
    'amused',
    'wrestle',
    'dogs',
    'cultured',
    'health',
    'act',
    'credit',
    'feeling',
    'flashy',
    'gun',
    'itch',
    'waiting',
    'call',
    'yarn',
    'waves',
    'beds',
    'unarmed',
    'absorbing',
    'boil',
    'productive',
    'able'
]

# class WordGenerator
class WordGenerator:

    # attributes
    def __init__(self):
        self.data = WORDS
        self.randomWord = choice(self.data)
        self.emptyList = []

    # creating empty list
    def creatingEmptyList(self):
        for i in range(0, len(self.randomWord)):
            self.emptyList.append('[ _ ]')

        return self.emptyList







