
def age_to_int(num):
    return int(num)

def time_to_int(time):
    hour_list = time.split(':')
    h = int(hour_list[0])
    m = int(hour_list[1])
    s = int(hour_list[2])


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

    print(artistsDict)  
    print('\n')   

    print(sort(artistsDict,"albumC"))  
    print (sort(artistsDict, "albumG"))  
    print (sort(artistsDict, "ageO"))
    print (sort(artistsDict, "ageY"))


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
        print("shitzu")

    if parameter == "albumS":
        print("Sort by small lenght") 

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

