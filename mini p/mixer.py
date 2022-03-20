from pygame import mixer
import time
mixer.init()

# Loading the song
mixer.music.load("story.mp3")

# Setting the volume
mixer.music.set_volume(1)

# Start playing the song
mixer.music.play()
while True:
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")

    query = input("  ")

    if query == 'p':

        # Pausing the music
        #mixer.music.fadeout(3000)
        #time.sleep(3)
        mixer.music.pause()

    elif query == 'r':

        # Resuming the music
        mixer.music.unpause()
        #mixer.sound.set_volume(1.0)


    elif query == 'e':

        # Stop the mixer
        mixer.music.stop()
        break
