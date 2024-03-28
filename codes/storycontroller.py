'''
Controls the storylines
'''
from . import init
import json
class story_controller:
    def __init__(self,story_name:str,main:init.inital) -> None:
        self.story=story_name
        self.game_instance=main
        self.config_status=main.config_exist
    def read_story():
        story_path:str="./story"+self.
