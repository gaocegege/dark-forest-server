__author__ = 'codeworm96'

from random import randint

lowBound = -500
highBound = 500

class Player:
    def __init__(self):
        self.x = randint(lowBound, highBound)
        self.y = randint(lowBound, highBound)
        self.alive = True
        self.current_version = 0

        
