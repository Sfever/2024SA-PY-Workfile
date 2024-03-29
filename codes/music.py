import time
import pydub
import os
import pydub.playback
from multiprocessing import Process

class MusicPlayer:
    def __init__(self):
        self.music_type = "mp3"
        self.music_path = ""
        self.player_thread = None
        self.play_obj = None

    def set_path(self, path):
        self.music_path = path
        self.music_type = os.path.splitext(path)[1][1:]
    def play_music(self):
        music_instance = pydub.AudioSegment.from_file(self.music_path, self.music_type)
        pydub.playback.play(music_instance)
    def play(self):
        self.player_thread = Process(target=self.play_music)
        self.player_thread.start()
        time.sleep(1)

    def stop(self):
        if self.player_thread is not None:
            self.player_thread.terminate()
            self.player_thread = None
