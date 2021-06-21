import numpy as np
from dice import Dice

class GameRound:

    def __init__(self):
        self.num_dice = 5
        self.saved_dice = []
        self.dice_in_play = []
        self.round_end = False

        self.buildDiceSet()

    def buildDiceSet(self):
        dice_arr = [Dice() for val in range(1, self.num_dice+1)]
        self.dice_in_play = dice_arr

    def rollDice(self):
        for die in self.dice_in_play:
            die.rollDice()

    def removeDieFromPlay(self, i):
        self.num_dice -= 1
        die_removed = self.dice_in_play.pop(i)
        self.saved_dice.append(die_removed)

    def endRound(self):
        if len(self.saved_dice) ==5:
            self.round_end = True
        return self.round_end
        
    def getDiceInPlay(self):
        return self.dice_in_play

    def getDiceInPlay(self):
        return self.dice_in_play

    def getSavedDice(self):
        return self.saved_dice

    def getDiceInPlayValues(self):
        v = self.getValues(self.dice_in_play)
        return v

    def getSavedDiceValues(self):
        v = self.getValues(self.saved_dice)
        return v

    def getValues(self, dice_array):
        v = []
        for dice in dice_array:
            v.append(dice.getDiceValue())
        return v

    

    
