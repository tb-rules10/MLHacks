import time
from pygame import mixer


mixer.init()
mixer.music.load("C:/Users/tanis/Downloads/The Game Of Thrones Theme Song Fender Custom Shop Fender.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)
    
    
