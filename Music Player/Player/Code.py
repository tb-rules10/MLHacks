from pygame import mixer

def showMusic():
    print("\nTB's Music Player 🎧\n")
    global d1
    d1 = {1: "Tu Aake Dekhle", 2: "Ranjha", 3: "Ek Raat",
          4: "Tum Kyu Chale Aate Ho", 5: "Mann Mera", 6: "Beggin", 7: "Venom",
          8: "What a Time", 9: "Arcade", 10: "GOT-Theme Song"}
    for key, value in d1.items():
        print("{} \t {}".format(key, value))
    print("\nCommands:-\nEnter 0 to exit || 1 to pause/unpause || 2 to select a new song ")


def selectMusic():
    x = int(input("\nEnter Your Song - "))
    str = d1[x] + ".mp3"
    return str


def playMusic(x):
    mixer.init()
    mixer.music.load(x)
    # print("Playing :", end=" ")
    mixer.music.play()
    c = input("Enter commands below:-\n")
    while mixer.music.get_busy():
        if c=='1':
            mixer.music.pause()
            cmd = input()
            if cmd=='1':
                mixer.music.unpause()
            else:
                return cmd
        else :
            mixer.music.stop()
            return c;


def main():
    showMusic()
    while 1:
        str = selectMusic()
        choice = playMusic(str)
        if choice == '0':
            exit(0)
        else:
            continue

main()
