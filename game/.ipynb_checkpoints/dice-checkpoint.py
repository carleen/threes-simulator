'''
Class for dice object
'''
import numpy as np

class Dice:

    def __init__(self):
        self.value = 0
        self.keep_dice = False

    def rollDice(self):
        self.value = np.random.randint(1,7)

    def getDiceValue(self):
        return self.value

    def keepDice(self):
        self.keep_dice = True

    def isKeepDice(self):
        return self.keep_dice

