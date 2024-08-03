#This is a basic implementation of a music player application inspired by cmus. Right now it works, but I want your help extending it.

import os
from pathlib import Path
import sys
import subprocess


class MusicPlayer:
    def __init__(self):
        self.home_dir = str(Path.home())
        self.music_dir = 'Music/Ariana Grande - thank u, next (2019) [320]' 
        self.music_dir = self.home_dir +'/'+ self.music_dir
        self.current_song = None

    def load_songs(self):
        songs = []
        songs = [str(self.music_dir+'/'+song) for song in os.listdir(self.music_dir)]
        return songs

    def startfile(self, song):
        subprocess.call(['xdg-open', song])

    def play_song(self, song):
        self.current_song = song
        self.startfile(self.current_song)


if __name__ == "__main__":
    player = MusicPlayer()
    songs = player.load_songs()
    if len(songs) > 0:
        player.play_song(songs[0])
    else:
        print("No songs found in directory")



"""
This code sets up a basic music player application that can load and play MP3 files in the specified directory. 
Please improve it by adding a command-line interface that allows for features such as skipping to the next or previous song, pausing and resuming playback.
"""