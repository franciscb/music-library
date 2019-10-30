import tkinter as tkt
#from play_internet import *


import vlc

screen = tkt.Tk()

p = vlc.MediaPlayer("http://192.168.0.88/Atreyu_Becoming,The,Bull_2007.mp3")

def stats_n():
    import stats
    del(stats)

def play_test():
    
   
    
    if p.is_playing() == False:
        p.play()


def stop_test():

    if p.is_playing() == True:
        p.pause()

screen.geometry("500x500")
screen.title("Music Shitzu Beach")
screen.resizable(False, False)



title = tkt.Label(screen, text ="Menu_test", bg ='#1e2021', fg = "white", font =("verdana",18))
title.pack(fill = "both")

playNet = tkt.Button(screen, width = 20 , text = "Play from URL", bg = '#1e2021', fg = 'white', relief = "raised", font =("verdana",10), command = play_test)
playNet.place(x = 170, y = 150)

playNet2 = tkt.Button(screen, width = 20 ,text = "Stop Sith from URL", bg = '#1e2021', fg = 'white', relief = "raised", font =("verdana",10), command = stop_test)
playNet2.place(x = 170, y = 180)






stats = tkt.Button(screen, width = 20 ,text = "Stats and Sith", bg = '#1e2021', fg = 'white', relief = "raised", font =("verdana",10), command = stats_n)
stats.place(x = 170, y = 250)

screen.mainloop()