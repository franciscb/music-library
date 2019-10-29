


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

def sort(lst,parameter=""):

    genre_album = {}
    if parameter == "ageY":
        print("Sort by young age")


    if parameter == "ageO":
        print("Sort by old age") 


    if parameter == "albumL":
         print("Sort by short lenght")

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
    return '***'        

readList()        

