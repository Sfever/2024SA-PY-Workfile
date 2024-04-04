from . import heros 
from . import player 
import json
class CharacterController:
    def __init__(self,storyname) -> None:
        self.configPath="./story"+storyname+"/characters.json"
    def _ReadConfig(self):
        with open(self.configPath,"r") as character_reader:
            self.character_config=json.load(character_reader)
    def CharacterInitalize(self):
        self._ReadConfig()
        self.heroList:list[heros.Hero]=[]
        self.playerList:list[player.Player]=[]
        for i in self.character_config["player"]:
            self.playerList.append(i)
        for i in self.character_config["heros"]:
            self.heroList.append(i)
