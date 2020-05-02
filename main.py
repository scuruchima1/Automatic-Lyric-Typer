import pynput
import time 
import lyricwikia
# (pip3 install lyricwikia)
# (pip3 install pynput)

from pynput.keyboard import Key, Controller
#Asks for song and artist
artist = input("artist: ") 
song = input("song: ")
# Delay from input of song to lyric typing
delay = 3

keyboard = Controller()
# Uses lyricwikia API to get lyrics 
lyrics = lyricwikia.get_lyrics(artist, song)
# Types lyrics
time.sleep(delay)
keyboard.type(lyrics)
keyboard.press(Key.enter)
