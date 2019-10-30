import vlc
import time
import sys




def play_audio(audio):
  if audio.is_playing() == False:
    audio.play()

  if audio.is_playing() == True:
    audio.pause() 
