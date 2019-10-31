import tkinter as tkt
#from play_internet import *
import subprocess 

def win_init():
    
    screen = tkt.Tk()

    screen.geometry("400x70+690+250")
    screen.title("Codecool Music Library")
    screen.resizable(False, False)

    def kill_wind():
        screen.destroy()


    err_mess = tkt.Label(screen, text ="IMPORT ERROR", bg ='#1e2021', fg = "RED", font =("verdana",12,"bold"))
    err_mess.pack(fill = "both")

    err_disp = tkt.Label(screen, text ="This combination of values appears to already be present in the DB",  fg = "black", font =("verdana",7,"bold"))
    err_disp.pack(fill = "both")


    k_but = tkt.Button(screen, text = "OK", bg = "gray", fg = "white", font = ("verdana", 8), command = kill_wind)
    k_but.pack()
    screen.mainloop()

    

win_init()