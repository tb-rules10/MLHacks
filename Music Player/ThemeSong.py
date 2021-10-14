import time
from pygame import mixer

print("\nTB's Music Player\n")

d1 = {1: "Tu Aake Dekhle", 2: "Ranjha", 3: "Ek Raat",
      4: "Tum Kyu Chale Aate Ho", 5: "Mann Mera", 6:"Beggin", 7: "Venom",
      8: "What a Time", 9: "Arcade", 10: "GOT-Theme Song"}

for key, value in d1.items():
    print ("{} \t {}".format(key,value))

x = int(input("\nEnter Your Song - "))
str = d1[x] + ".mp3"
print(str)

mixer.init()
mixer.music.load(str)
print("Playing :", end=" ")
mixer.music.play()

print ("Enter 0 to stop")
while mixer.music.get_busy():
    exit(input())# wait for music to finish playing
    time.sleep(1)
    
