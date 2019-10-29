import vlc
import time

p = vlc.MediaPlayer("http://localhost/Atreyu_Becoming,The,Bull_2007.mp3")  # local host to be changed to actual local ip eg 192.168.0.808

p.play()
time.sleep(.5)     #  time buffer used to ensure the player is loading.
while p.is_playing():
     time.sleep(1)

