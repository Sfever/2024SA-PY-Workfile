'''
Everything you need about player
'''
class Player:
    def __init__(self) -> None:
        self.name=""
        self.energy=0
        self.literature=0
        self.technology=0
        self.arts=0
        self.sport=0
        self.attract=0
        self.look=0
        self.preseverance=0
        self.pressure=0
        self.money=0
'''
Detailed Explain:
this is the attributes of the character, all those values are read from a json file and can be muniplated with in the game
all those values affects the heros' attitude towards player and game events
There is no limit of these values' range, but set them too high will crash the python interpreter because of the 32bit integer limit(Longer integers will not be considered because they're meaningless and doesn't help so much)
'''