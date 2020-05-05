import pygame
import time
from pygame import mixer
pygame.mixer.init()
pygame.init()
mixer.music.load("sound.mp3")

def alarm():
    pygame.mixer.init()
    pygame.init()

    hor = int(input("enter the hour: "))
    minn = int(input("enter tsshe minute: "))
    sec = int(input("enter the second: "))

    n =5

    print("alarm set for" + str(hor) + ":" + str(minn)+ ":" + str(sec))
    while True:
        if time.localtime().tm_hour==hor and time.localtime().tm_min==minn and time.localtime().tm_sec==sec:
            print("wake up")
            break

    while n>0:
        mixer.music.play()
        time.sleep(2)
        n = n-1

    sn = str(input("press s for snooze"))
    if sn == 's':
        n=3
        time.sleep(100)
        while n>0:
            mixer.music.play()
            time.sleep(2)

    else:
        exit()


alarm()