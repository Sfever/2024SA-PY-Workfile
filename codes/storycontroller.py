'''
Controls the storylines
'''
from codes.player import Player
from . import init
import json
import random
class StoryController:
    def __init__(self,story_name:str,main:init.inital) -> None:
        self.story=story_name
        self.gameInstance=main
        self.configStatus=main.configExist
        self.storyContent={}
        self.levels=[None,]
        self.currentlevel=1
        self._ReadStory(main)
        self._LoadLevel()
    def _ReadStory(self,main:init.inital):
        self.storyPath:str="./story"+self.story
        if self.configStatus==1:
            storyPath=main.GetConfig()
            self.storyPath=storyPath["StoryPath"] # type: ignore
        with open(self.storyPath,"r") as storyReader:
            self.storyContent=json.load(storyReader)
    def _LoadLevel(self):
        for i in self.storyContent.values():
            self.levels.append(i)
    def _GetLevel(self,level)->dict:
        return self.levels[level]
    def _GetLevelData(self,level)->list[dict]:
        leveldata=self._GetLevel(level)
        options=[{},]
        for i in leveldata.values():
            options.append(i)
        return options
    def _GetOptionData(self,level,option):
        leveldata=self._GetLevelData(level=level)
        optiondata:dict=leveldata[option]
        optionRequirements:list=optiondata["requirements"]
        optionText=optiondata["text"]
        optionImage=optiondata["Images"]
        return [optionRequirements,optionText,optionImage]
    def _CheckOptionAvailbility(self,player:Player,level,option):
        optiondata=self._GetOptionData(level,option)
        satisfied=True
        playerdata=player.GetData()
        for i in range(len(playerdata)):
            if playerdata[i]<optiondata[i]:
                satisfied=False
                break
        return satisfied
    def MoveLevel(self,player):
        self.currentlevel+=1
        availableOptions=[]
        for i in range(len(self._GetLevelData(self.currentlevel))):
            if self._CheckOptionAvailbility(player,self.currentlevel,i) == True:
                availableOptions.append(i)
        return availableOptions