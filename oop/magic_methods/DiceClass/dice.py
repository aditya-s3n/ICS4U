import random

class Die:
    def __init__(self, sides):
        self._sides = sides

    def roll(self):
        return random.randint(1, self._sides)
    
    def __str__(self):
        return f"Dice, {self._sides} sides"
    
    def __repr__(self):
        return f"Dice, {self._sides} sides"
    
    def __eq__(self, other):
        return self.roll() == other.roll()
    
    def __lt__(self, other):
        return self.roll() < other.roll()
    
    def __gt__(self, other):
        return self.roll() > other.roll()
    

#example of a program to use the Die class
die1 = Die(7)
die2 = Die(7)

#use the equality function
print(die1 == die2)

#use the less than function
print(die1 < die2)