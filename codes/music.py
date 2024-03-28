import pydub
import pydub.playback
import os
import threading

class MusicPlayer:
    def __init__(self):
        self.music_type = "mp3"
        self.music_path = ""
        self.player_thread = None
        self.stop_playback = threading.Event()

    def set_path(self, path):
        self.music_path = path
        self.music_type = os.path.splitext(path)[1][1:]

    def play(self):
        def play_music():
            music_instance = pydub.AudioSegment.from_file(self.music_path, self.music_type)
            while not self.stop_playback.is_set():
                pydub.playback._play_with_simpleaudio(music_instance)

        self.stop_playback.clear()
        self.player_thread = threading.Thread(target=play_music)
        self.player_thread.start()

    def stop(self):
        if self.player_thread is not None:
            self.stop_playback.set()
            self.player_thread.join()
            self.player_thread = None
