import time
from pygame import mixer


mixer.init()
mixer.music.load("game-of-thrones-theme-song-ringtone-30782.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)

