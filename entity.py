import random

class Vampire():
    
    def __init__(self, pos, mapSize, health, stack):
        # The position of the Vampire as x & y values stored in a list
        #stack for "met somthing before, skip function"
        self.pos = pos
        self.mapSize = mapSize
        self.health = health
        self.stack = stack
        
    
    def stepChange(self):
        self.pos[0] += random.randint(-8, 8)
        self.pos[1] += random.randint(-8, 8)

        # If the Vampire moved off the map, move it back on
        if self.pos[0] < 0:
            self.pos[0] = 0
        elif self.pos[0] >= self.mapSize[0]:
            self.pos[0] = self.mapSize[0]
        
        if self.pos[1] < 0:
            self.pos[1] = 0
        elif self.pos[1] >= self.mapSize[1]:
            self.pos[1] = self.mapSize[1]
        

class Human():
    
    def __init__(self, pos, mapSize, health, age, stack):
        # The position of the Human as x & y values stored in a list
        self.pos = pos
        self.mapSize = mapSize
        self.health = health
        self.age = age
        self.stack = stack
    
    def stepChange(self):
        self.pos[0] += random.randint(-4, 4)
        self.pos[1] += random.randint(-4, 4)

        # If the Human moved off the map, move it back on
        if self.pos[0] < 0:
            self.pos[0] = 0
        elif self.pos[0] >= self.mapSize[0]:
            self.pos[0] = self.mapSize[0]
        
        if self.pos[1] < 0:
            self.pos[1] = 0
        elif self.pos[1] >= self.mapSize[1]:
            self.pos[1] = self.mapSize[1]
        
class Water():
    
    def __init__(self, pos, mapSize):
        # The position of the Human as x & y values stored in a list
        self.pos = pos
        self.mapSize = mapSize
    
    def getLocation(self):
        return self.pos

class Food():
    
    def __init__(self, pos, mapSize):
        # The position of the food as x & y values stored in a list
        self.pos = pos
        self.mapSize = mapSize
    
    def getLocation(self):
        return self.pos
        
class Garlic():
    
    def __init__(self, pos, mapSize):
        # The position of the Garlic as x & y values stored in a list
        self.pos = pos
        self.mapSize = mapSize
        
    
    def getLocation(self):
        return self.pos

