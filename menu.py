#!/usr/bin/env python3
import tkinter as tkt
#from play_internet import *
import subprocess 
import vlc
import time as tm
import requests as req

def win_init():
    screen = tkt.Tk()

    audio = vlc.MediaPlayer("http://localhost/Atreyu_Becoming,The,Bull_2007.mp3")    #192.168.0.88

    def go_places():
        subprocess.call(['python3', 'import_to_db.py'])


    def go_to_radio():
        try:
            server = req.get("http://localhost")
            screen.destroy()
            subprocess.call(['python3', 'radio_menu.py'])
            print(server) 
        except req.ConnectionError:
            connection_error()
            print("Stuff aint working man!")      

    def connection_error():
        tm.sleep(1)
        screen.withdraw()
        subprocess.call(['python3', 'err_connect.py'],)
        screen.deiconify()
        #reopen_buttons()
        
    def stop_test():
        if audio.is_playing() == True:
            audio.pause() 
            playNet2["state"] = "disabled"
            playNet["state"] = "normal"


    def close_win():
        screen.destroy()

    def stats_n():
        tm.sleep(1)
        screen.withdraw()
        subprocess.call(['python3', 'stats.py'])
        screen.deiconify()
        


    def reopen_buttons():
        playNet["state"] = "normal"
        playNet2["state"] = "normal"
        stats["state"] = "normal"
        stats1["state"] = "normal"
        if audio.is_playing() == True:
            playNet2["state"] = "normal"
            playNet["state"] = "disabled"

        elif audio.is_playing() == False:
            playNet["state"] = "normal"
            playNet2["state"] = "disabled"


    def call_alpha():
        screen.withdraw()
        subprocess.call(['python3', 'alpha_b.py'])
        screen.deiconify()




    screen.geometry("500x500+650+250")
    screen.title("Codecool Music Library")
    screen.resizable(False, False)



    title = tkt.Label(screen, text ="Main Menu", bg ='#1e2021', fg = "white", font =("verdana",18))
    title.pack(fill = "both")

    playNet = tkt.Button(screen, width = 16 , text = "Display Local DB", bg = '#1e2021', fg = 'white', relief = "raised"  ,font =("verdana",10), command = call_alpha )

    playNet.place(x = 170, y = 150)

    playNet2 = tkt.Button(screen, width = 16 ,text = "Internet Radio ", bg = '#1e2021', fg = 'white',state = "normal",  relief = "raised"  ,font =("verdana",10), command = go_to_radio)
    playNet2.place(x = 170, y = 180)






    stats = tkt.Button(screen, width = 16 ,text = "Database Stats", bg = '#1e2021', fg = 'white', relief = "raised", font =("verdana",10), command = stats_n)
    stats.place(x = 170, y = 250)


    stats1 = tkt.Button(screen, width = 16 ,text = "Add to database", bg = '#1e2021', fg = 'white', relief = "raised", font =("verdana",10), command = lambda:[stop_test(), close_win(),go_places()])
    stats1.place(x = 170, y = 290)

    screen.mainloop()

win_init()   