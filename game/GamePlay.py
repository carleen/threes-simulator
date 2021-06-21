from dice import Dice
from DiceHand import DiceHand

class GamePlay:

    def __init__(self, dice_hand):
        self.dice_hand = dice_hand
        self.round_end = False

    def chooseDiceToKeep(self):
        ind_to_keep  = []
        p = self.dice_hand.getDiceInPlayValues()

        for i in range(0, len(p)):
            if p[i]==3:
                ind_to_keep.append(i)

        if len(ind_to_keep) == 0:
            min_val = min(p)
            i = p.index(min_val)
            ind_to_keep.append(i)

        return ind_to_keep
        
    def keepRemoveDice(self, ind_to_keep):
        ind_augment = 0
        for die_ind in ind_to_keep:
            self.dice_hand.removeDiceFromPlay(die_ind-ind_augment)
            ind_augment +=1
        if len(self.dice_hand.dice_in_play) == 0:
            self.round_end = True

    def getScore(self):
        score = 0
        dice_saved = self.dice_hand.getSavedDiceValues()
        for die in dice_saved:
            if die == 3:
                score+=0
            else:
                score+=die
        return score

    def restartRound(self):
        self.round_end = False 
        self.dice_hand.resetDice()

        
