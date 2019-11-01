import tkinter as tkt
import subprocess 
import time as tm
import requests as req
import vlc 
import random as ra


def win_init():

    screen = tkt.Tk()
    screen.geometry("500x500+650+250")
    screen.title("Codecool Music Library")
    screen.resizable(False, False)

    text = req.get('http://localhost/metalcore/metalcore_url.txt')

    with open("metalcore_url.txt", 'wb') as getnet:
        getnet.write(text.content)

    with open("metalcore_url.txt") as song_play:
        songs = song_play.readlines()

    for i in range(len(songs)):
        songs[i] = songs[i].rstrip('\n')

    def exit_this():
        
        try:
            
            current_song.stop()
            screen.destroy()
            subprocess.call(['python3', 'menu.py'])
            
        except NameError:
            
            screen.destroy()
            subprocess.call(['python3', 'menu.py'])
           
        

    def connection_error():
        tm.sleep(1)
        screen.withdraw()
        subprocess.call(['python3', 'err_connect.py'],)
        screen.deiconify()    

    def next_song():
        try:
            server = req.get("http://localhost")
            current_song.stop()
            get_play()
        except req.ConnectionError:
            current_song.stop()
            connection_error()
            print("Stuff aint working man!")     
    
    def pause():
        try:
            server = req.get("http://localhost")
            current_song.pause()
        except req.ConnectionError:
            connection_error()
            print("Stuff aint working man!")     

        

    def get_play():
        try:
            server = req.get("http://localhost")
            rad_2["state"] = "normal"
            rad_1["state"] = "disabled"
            rad_3["state"] = "normal"
            if len(songs) > 0:
                ra.shuffle(songs)
                tm.sleep(1)
                global current_song
                current_song = songs.pop(0)
                current_song = str(current_song)
                print (current_song,type(current_song))
                current_song = vlc.MediaPlayer(current_song)
                tm.sleep(.5)
                current_song.play()
            else:
                exit_this()    
        except req.ConnectionError:
            connection_error()
            print("Stuff aint working man!")      
        

    title = tkt.Label(screen, text ="Internet Radio", bg ='#1e2021', fg = "white", font =("verdana",18))
    title.pack(fill = "both")

    rad_1 = tkt.Button(screen, text = "Urlete Playlist!", bg = 'red' , fg = 'white', font =("verdana",14), state = "active", command = get_play) 
    rad_1.place(x = 50, y = 70)

    rad_2 = tkt.Button(screen, text = "Next", bg = '#375d7d' , fg = 'white', state = 'disabled', font =("verdana",16), command = next_song) 
    rad_2.place(x = 240, y = 70)


    rad_3 = tkt.Button(screen, text = "Pause/Play", bg = '#c45c1b' , fg = 'white', font =("verdana",13), state = 'disabled', command = pause) 
    rad_3.place(x = 220, y = 150)

    #rad_4 = tkt.Label(screen, text = "Resume", bg = '#4d9109', fg = 'white', font = ("verdana",16),)
    #rad_4.place(x = 240, y = 150)
    
    ext_butt = tkt.Button(screen, text = "Exit", bg = 'black', fg = 'white', font = ("verdana",18), command = exit_this )
    ext_butt.place(x = 200, y = 400)
    screen.mainloop()


win_init()