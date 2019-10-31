import tkinter as tkt
#from play_internet import *
import subprocess 
import vlc
import time as tm
import requests as req

def win_init():
    screen = tkt.Tk()

    audio = vlc.MediaPlayer("http://192.168.0.88/Atreyu_Becoming,The,Bull_2007.mp3")    #192.168.0.88
    def play_test():
        if audio.is_playing() == False:
            
            try:
                server = req.get("http://192.168.0.88")
                audio.play()
                print(server)
                playNet["state"] = "disabled"
                playNet2["state"] = "normal"
                    
            except req.ConnectionError:
                
                connection_error()
                print("Stuff aint working man!") 

    def go_places():
        subprocess.call(['python3', 'new_s.py'])

    def connection_error():
        playNet["state"] = "disabled"
        playNet2["state"] = "disabled"
        stats["state"] = "disabled"
        stats1["state"] = "disabled"
        tm.sleep(1)
        subprocess.run(['python3', 'err_connect.py'], )
        #reopen_buttons()
        
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
        tm.sleep(1)
        subprocess.call(['python3', 'stats.py'])
        


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







    screen.geometry("500x500+650+250")
    screen.title("Codecool Music Library")
    screen.resizable(False, False)



    title = tkt.Label(screen, text ="Main Menu", bg ='#1e2021', fg = "white", font =("verdana",18))
    title.pack(fill = "both")

    playNet = tkt.Button(screen, width = 16 , text = "Play Local", bg = '#1e2021', fg = 'white', relief = "raised"  ,font =("verdana",10), command =lambda:[play_test(),reopen_buttons()])

    playNet.place(x = 170, y = 150)

    playNet2 = tkt.Button(screen, width = 16 ,text = "Internet Radio ", bg = '#1e2021', fg = 'white',state = "disabled",  relief = "raised"  ,font =("verdana",10), command = stop_test)
    playNet2.place(x = 170, y = 180)






    stats = tkt.Button(screen, width = 16 ,text = "Database Stats", bg = '#1e2021', fg = 'white', relief = "raised", font =("verdana",10), command = lambda:[stats_n(),reopen_buttons()])
    stats.place(x = 170, y = 250)


    stats1 = tkt.Button(screen, width = 16 ,text = "Add to database", bg = '#1e2021', fg = 'white', relief = "raised", font =("verdana",10), command = lambda:[stop_test(), close_win(),go_places()])
    stats1.place(x = 170, y = 290)

    screen.mainloop()
    reopen_buttons()

win_init()   