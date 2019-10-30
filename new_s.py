import tkinter as tkt

import subprocess



def win_init():
    screen2 = tkt.Tk()


    
    screen2.geometry("500x500+650+250")
    screen2.title("SOme other Sith")
    screen2.resizable(False, False)

    def close_win2():
        screen2.destroy()

    def get_back():
        
        subprocess.run(['python3', 'menu.py'])


    title = tkt.Label(screen2, text ="New_win_test", bg ='#1e2021', fg = "white", font =("verdana",18))
    title.pack(fill = "both")


    return_to_sender = tkt.Button(screen2, text ="Return to the previous sith", fg = "white", relief = "raised", bg = "red", font = ("verdana", 18), command = lambda:[close_win2(), get_back()])
    return_to_sender.place(x = 70, y=250)
    
    screen2.mainloop()
    

win_init()    