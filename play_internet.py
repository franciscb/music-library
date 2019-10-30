import vlc
import time

  # local host to be changed to actual local ip eg 192.168.0.808
def play_test(p):
   
    p.play()
    while p.is_playing() == True:
        #p.play()
        #time.sleep(.5)     #  time buffer used to ensure the player is loading.
        #while p.is_playing():
        time.sleep(1)
        #print(p.play())

