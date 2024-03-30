import time
import pydub
import os
import pydub.playback
from multiprocessing import Process

class MusicPlayer:
    def __init__(self):
        self.music_type = "mp3"
        self.music_path = ""
        self.player_process = None
        self.play_obj = None

    def SetPath(self, path):
        self.music_path = path
        self.music_type = os.path.splitext(path)[1][1:]
    def _PlayMusic(self):
        music_instance = pydub.AudioSegment.from_file(self.music_path, self.music_type)
        pydub.playback.play(music_instance)
    def Play(self):
        self.player_process = Process(target=self._PlayMusic)
        self.player_process.start()
        time.sleep(1)

    def Stop(self):
        if self.player_process is not None:
            self.player_process.terminate()
            self.player_process = None
