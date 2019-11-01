

import tkinter as tkt
import subprocess
import time




def win_init():


    screen = tkt.Tk()
    screen.geometry("500x500+650+250")
    screen.title("Codecool Music Library - Import File")
    screen.resizable(False, False)

   
    #print(new_lst)    

    
    def write_to_file():
        print("{} {} {} {} {}".format(band_name_value.get(),album_name_value.get(), year_value.get(), genre_name_value.get(), time_len_value.get()))
        bnd = band_name_value.get()
        alb = album_name_value.get()
        with open('text_albums_data.txt') as check_lst:
            new_lst = check_lst.readlines()
                
        for i in range(len(new_lst)):
            new_lst[i] = new_lst[i].split(',')
        for i in range(len(new_lst)):
            if bnd == new_lst[i][0] and alb == new_lst[i][1]:
                subprocess.call(['python3', 'in_db.py'])
                return ''
        str_to_write = "{},{},{},{},{}".format(band_name_value.get(),album_name_value.get(), year_value.get(), genre_name_value.get(), time_len_value.get())
        with open("text_albums_data.txt",'a') as fll:
            fll.writelines( str_to_write + '\n')

    def get_reset():
        band_name_value.delete(0, "end")
        album_name_value.delete(0, "end")
        year_value.delete(0, "end")
        genre_name_value.delete(0, "end")
        time_len_value.delete(0, "end")

    def write_reset():
        print("{} {} {} {} {}".format(band_name_value.get(),album_name_value.get(), year_value.get(), genre_name_value.get(), time_len_value.get()))
        bnd = band_name_value.get()
        alb = album_name_value.get()
        with open('text_albums_data.txt') as check_lst:
            new_lst = check_lst.readlines()
                
        for i in range(len(new_lst)):
            new_lst[i] = new_lst[i].split(',')
        for i in range(len(new_lst)):
            if bnd == new_lst[i][0] and alb == new_lst[i][1]:
                subprocess.call(['python3', 'in_db.py'])
                return ''
        #print(alb, bnd, type(alb), type(bnd)) 
        str_to_write = "{},{},{},{},{}".format(band_name_value.get(),album_name_value.get(), year_value.get(), genre_name_value.get(), time_len_value.get())
        with open("text_albums_data.txt",'a') as fll:
            fll.writelines(str_to_write + '\n')
        get_reset()


    def go_places():
        subprocess.call(['python3', 'menu.py'])

    def kill_wind():
        screen.destroy()    


    title = tkt.Label(screen, text ="Database Import Menu", bg ='#1e2021', fg = "white", font =("verdana",18))
    title.pack(fill = "both")
    band_name = tkt.Label(screen, text = "Band Name:",relief = "raised",  font = ("verdana", 12), bd = 4)
    band_name.place(x = 70, y = 150)
    band_name_value = tkt.Entry(screen , bd = 5,  bg = "white")
    band_name_value.place(x = 190, y = 150)

    album_name = tkt.Label(screen, text = "Album Name:",relief = "raised",  font = ("verdana", 11), bd = 4)
    album_name.place(x = 70, y = 190)
    album_name_value = tkt.Entry(screen ,  bd = 5,  bg = "white")
    album_name_value.place(x = 190, y = 190)


    year = tkt.Label(screen, text = "Year:",relief = "raised",  font = ("verdana", 13), bd = 4)
    year.place(x = 70, y = 230)
    year_value = tkt.Entry(screen ,  bd = 5,  bg = "white")
    year_value.place(x = 190, y = 230)



    genre_name = tkt.Label(screen, text = "Genre:",relief = "raised",  font = ("verdana", 13), bd = 4)
    genre_name.place(x = 70, y = 270)
    genre_name_value = tkt.Entry(screen ,  bd = 5,  bg = "white")
    genre_name_value.place(x = 190, y = 270)


    time_len = tkt.Label(screen, text = "Time:",relief = "raised",  font = ("verdana", 13), bd = 4)
    time_len.place(x = 70, y = 310)
    time_len_value = tkt.Entry(screen ,  bd = 5,  bg = "white")
    time_len_value.place(x = 190, y = 310)

    add_to_file =tkt.Button(text = "Add to Database", bg = "green", fg = "white", font = ("Verdana", 8), command = write_to_file)
    add_to_file.place(x = 70, y = 380)

    add_to_reset = tkt.Button(text = "Add to Database and reset form", bg = "red", fg = "white", font = ("Verdana", 8), command = write_reset)
    add_to_reset.place(x = 210, y = 380)


    go_back = tkt.Button(text = "Go Back", bg = "black", fg = "white", font = ("Verdana", 8), command = lambda:[kill_wind(), go_places()])
    go_back.place(x = 250, y = 410)

    screen.mainloop()


win_init()    

