import os
from pathlib import Path
import sys
import subprocess


class MusicPlayer:
    def __init__(self):
        self.home_dir = str(Path.home())
        self.music_dir = 'Music/Ariana Grande - thank u, next (2019) [320]' 
        self.music_dir = self.home_dir +'/'+ self.music_dir
        self.all_songs = []
        self.current_song = None

    def load_songs(self):
        songs = []
        try:
            for root, dirs, files in os.walk(self.music_dir):
                for file in files:
                    if file.endswith(".mp3") or file.endswith(".wav"):
                        song_path = str(Path(root) / file)
                        songs.append(song_path)
        except Exception as e:
            print(f"Error loading songs: {str(e)}")
        songs.sort()
        return songs

    def startfile(self, song):
        try:
            subprocess.call(['xdg-open', song])
        except Exception as e:
            print(f"Error playing song: {str(e)}")

    def play_song(self, song):
        self.current_song = song
        self.startfile(self.current_song)

    def mov_index(self, move_by):
        # Assume we have a list of songs loaded in the MusicPlayer instance
        # move_by can be positive or negative
        songs = self.all_songs
        current_index = songs.index(self.current_song)
        new_index = (current_index + move_by) % len(songs)
        return new_index

    def ui(self):
        songs = self.all_songs
        while True:
            com = input('Change song: ')
            print(com)
            if len(com) == 0:
                break
            if com == 'n' or com == 'N':
                num = 1
            elif com == 'p' or com == 'P':
                num = -1
            else: 
                num = int(com)
            new_index = self.mov_index(num)
            print(num, new_index)
            self.play_song(songs[new_index])

    def next(self):
        next_index = self.mov_index(1)
        # Play the next song in the list
        self.play_song(songs[next_index])

    def prev(self):
        prev_index = self.mov_index(-1)
        # Play the previous song in the list
        self.play_song(songs[prev_index])


def pause_playback():
    # Add code to pause playback of the current song
    pass

def resume_playback():
    # Add code to resume playback of the paused song
    pass


if __name__ == "__main__":
    player = MusicPlayer()
    player.all_songs = player.load_songs()
    player.play_song(player.all_songs[0])
    player.ui()


