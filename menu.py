import tkinter as tkt
#from play_internet import *
import subprocess 
import vlc
import time as tm

def win_init():
    screen = tkt.Tk()

    audio = vlc.MediaPlayer("http://192.168.0.88/Atreyu_Becoming,The,Bull_2007.mp3")

    def play_test():
        if audio.is_playing() == False:
            audio.play()
            playNet["state"] = "disabled"
            playNet2["state"] = "normal"
            
    def go_places():
        subprocess.call(['python3', 'new_s.py'])


    def stop_test():
        if audio.is_playing() == True:
            audio.pause() 
            playNet2["state"] = "disabled"
            playNet["state"] = "normal"


    def close_win():
        screen.destroy()

    def stats_n():
        playNet["state"] = "disabled"
        playNet2["state"] = "disabled"
        stats["state"] = "disabled"
        stats1["state"] = "disabled"
        tm.sleep(5)
        subprocess.call(['python3', 'stats.py'])
        


    def reopen_buttons():
        playNet["state"] = "normal"
        playNet2["state"] = "normal"
        stats["state"] = "normal"
        stats1["state"] = "normal"




    screen.geometry("500x500+650+250")
    screen.title("Music Shitzu Beaches")
    screen.resizable(False, False)



    title = tkt.Label(screen, text ="Menu_test", bg ='#1e2021', fg = "white", font =("verdana",18))
    title.pack(fill = "both")

    playNet = tkt.Button(screen, width = 16 , text = "Play from URL", bg = '#1e2021', fg = 'white', relief = "raised"  ,font =("verdana",10), command = play_test)

    playNet.place(x = 170, y = 150)

    playNet2 = tkt.Button(screen, width = 16 ,text = "Stop Sith from URL", bg = '#1e2021', fg = 'white',state = "disabled",  relief = "raised"  ,font =("verdana",10), command = stop_test)
    playNet2.place(x = 170, y = 180)






    stats = tkt.Button(screen, width = 16 ,text = "Stats and Sith", bg = '#1e2021', fg = 'white', relief = "raised", font =("verdana",10), command = lambda:[stats_n(),reopen_buttons()])
    stats.place(x = 170, y = 250)


    stats1 = tkt.Button(screen, width = 16 ,text = "Go east", bg = '#1e2021', fg = 'white', relief = "raised", font =("verdana",10), command = lambda:[stop_test(), close_win(),go_places()])
    stats1.place(x = 170, y = 290)

    screen.mainloop()

win_init()   