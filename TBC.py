
"""
tbcstart.py

@author: michael.scott
"""
class Character(object):
    
    def __init__(self):
        super().__init__()
        self.__name = "Default Name"
        self.__hitPoints = 10
        self.__armor = 2
        self.__hitChance = 60
        self.__maxDamage = 3
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property
    def hitPoints(self):
        return self.__hitPoints
    
    @hitPoints.setter
    def hitPoints(self, value):
        self.__hitPoints = value
        
    @property
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self, value):
        self.__armor = value
        
    @property
    def hitChance(self):
        return self.__hitChance
    
    @hitChance.setter
    def hitChance(self, value):
        self.__hitChance = value
    
    @property
    def maxDamage(self):
        return self.__maxDamage
    
    @maxDamage.setter
    def maxDamage(self, value):
        self.__maxDamage = value
        
    def testInt(self, value, min = 0, max = 100, default = 0):
    """ takes in value 
        checks to see if it is an int between
        min and max.  If it is not a legal value
        set it to default """

    out = default

    if type(value) == int:
        if value >= min:
            if value <= max:
                out = value 
            else:
                print("Too large")
        else:
            print("Too small")
    else:
        print("Must be an int")

    return out

    def printStats(self):
        print (f"""
 {self.name}
 hit points: {self.hitPoints}
 hit chance: {self.hitChance}
 max damage: {self.maxDamage}
 armor: {self.armor}""")
                
            







def main():
      c = Character()
      c.printStats()
    
    
    




main()





