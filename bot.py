#INTRODUCTION TO OBJECT ORIENTED PROGRAMMING(DECORATORS)

class Bot():#class names always start in CAPS

    _manufactured_bots = 0
    def __init__(self, name, catch_phrase = "Hi", avata_url = "https:"):#similar to constructor method in Python
        #parameters that are to be allocated default values should usually be at the end
        self.name = name
        self.health = 100
        self.damage = 0
        self.armor = 100
        Bot._manufactured_bots += 1

    def fire(self):
        print("Firing some shots")
    
    def getHealth(self):
        return self._health
    
    def setHealth(self):
        set._Health -= 5
    
    health = property(getHealth, setHealth)

asault_bot = Bot("Assault Bot1")
support_bot = Bot(name = "Support Bot1", avata_url = "https:")
defence_bot = Bot("KDF Bot")

print(asault_bot.health)
Bot.manufactured_bots += 1
print("Total bots manufactured", Bot.manufactured_bots)
#OBJECT INHERITANCE IN PYTHON