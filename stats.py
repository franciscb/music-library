import subprocess
def age_to_int(num):
    return int(num)

def time_to_int(time):
    if time.count(':') == 2:
        hour_list = time.split(':')
        h = int(hour_list[0])
        m = int(hour_list[1])
        s = int(hour_list[2])

        ms_time = (h * 3600) + (m*60) + s

        return ms_time

    elif  time.count(':') == 1:
        hour_list = time.split(':')
        m = int(hour_list[0])
        s = int(hour_list[1])

        ms_time = (m*60) + s
        return ms_time


def readList():

    artistsDict = {}
    with open ("text_albums_data.txt") as albm:
        musicDB  = albm.readlines()


    for item in range(len(musicDB)):
        musicDB[item] = musicDB[item].rstrip('\n')
        musicDB[item] = musicDB[item].split(',')
        if musicDB[item][0] in artistsDict.keys():
            artistsDict[musicDB[item][0]] += list((musicDB[item][1], musicDB[item][2], musicDB[item][3], musicDB[item][4]))
        
        else:
            artistsDict[musicDB[item][0]] = list((musicDB[item][1], musicDB[item][2], musicDB[item][3], musicDB[item][4]))
 
    print('\n')   

    print(sort(artistsDict,"albumC"))  
    print (sort(artistsDict, "albumG"))  
    print (sort(artistsDict, "ageO"))
    print (sort(artistsDict, "ageY"))
    print(sort(artistsDict, "albumL"))
    print(sort(artistsDict, "albumS"))
    subprocess.run(['gedit', 'README.md']) 

def sort(lst,parameter=""):

    genre_album = {}

    


    if parameter == "ageO":
        key_initial = list(lst.keys())
        key_initial = key_initial[0]
        year = age_to_int(lst[key_initial][1])
        i = 1
        for key in lst.keys():
            while i < len(lst[key]):
                year_check = age_to_int(lst[key][i])
                if year > year_check:
                    year = year_check
                i += 4
            i = 1 
        year = str(year)
        i = 1
        print("Oldest album(s):")
        for key in lst.keys():
            while i < len(lst[key]):
                if lst[key][i] == year:
                    print("{} by {} released in {}.".format(lst[key][i-1], key, year))
                i += 4 
            i = 1        
        return ""            

    if parameter == "ageY":
        key_initial = list(lst.keys())
        key_initial = key_initial[0]
        year = age_to_int(lst[key_initial][1])
        i = 1
        for key in lst.keys():
            while i < len(lst[key]):
                year_check = age_to_int(lst[key][i])
                if year < year_check:
                    year = year_check
                i += 4
            i = 1 
        year = str(year)
        i = 1
        print("Newest album(s):")
        for key in lst.keys():
            while i < len(lst[key]):
                if lst[key][i] == year:
                    print("{} by {} released in {}.".format(lst[key][i-1], key, year))
                i += 4 
            i = 1        
        return ""            


    if parameter == "albumL":
        key_initial = list(lst.keys())
        key_initial = key_initial[0]
        timespan = time_to_int(lst[key_initial][3])
        i = 3
        for key in lst.keys():
            while i < len(lst[key]):
                time_check = time_to_int(lst[key][i])
                if timespan < time_check:
                    timespan = time_check
                    time_str = lst[key][i]
                i += 4
            i = 3 
        i=3    
        print("Longest album(s):")
        for key in lst.keys():
            while i < len(lst[key]):
                if lst[key][i] == time_str:
                    print("{} by {} at {}.".format(lst[key][i-3], key, time_str))
                i += 4 
            i = 3        
        return ""           
        
    
    
    if parameter == "albumS":
        key_initial = list(lst.keys())
        key_initial = key_initial[0]
        timespan = time_to_int(lst[key_initial][3])
        i = 3
        for key in lst.keys():
            while i < len(lst[key]):
                time_check = time_to_int(lst[key][i])
                if timespan > time_check:
                    timespan = time_check
                    time_str = lst[key][i]
                i += 4
            i = 3 
        i=3    
        print("Shortest album(s):")
        for key in lst.keys():
            while i < len(lst[key]):
                if lst[key][i] == time_str:
                    print("{} by {} at {}.".format(lst[key][i-3], key, time_str))
                i += 4 
            i = 3        
        return ""    


    if parameter == "albumC":
        print("Number of albums ")
        i=0
        dbTotal = 0  
        for key in lst.keys():
            while i < len(lst[key]):
                dbTotal += 1
                i += 4
            i = 0 

        return dbTotal
    
    if parameter == "albumG":
        i=2 
        for key, val in lst.items():
            while i < len(lst[key]):
                if lst[key][i] in genre_album.keys():
                    genre_album[lst[key][i]] += 1
                else:
                    genre_album[lst[key][i]] = 1    
                i += 4
            i = 2   

        print('\n' + "--------------")        
        print("Album by genre")
        print("--------------" + '\n')
        for key, val in genre_album.items():
            upper_key = str(key)
            upper_key = upper_key.upper()
            print("Genre {} contains {} albums in database.".format(upper_key,val))
            print("-----------------------------------------------------------")
    return ""        
readList()        

