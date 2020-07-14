from pygame import mixer
import playsound
from time import sleep

def playText(sound_file):

    mixer.init()
    mixer.music.load(sound_file)
    mixer.music.play(999)
    while mixer.music.get_busy():
        sleep(1)
    print("Finished playing sound file")
    #playsound.playsound(sound_file, False)


if __name__ == '__main__':

    playText(sound_file='ch_test.mp3')
