


def readList():

    artistsDict = {}
    i = 0
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
    

def sort(lst,parameter=""):
    if parameter == "ageY":
        print("Sort by young age")


    if parameter == "ageO":
        print("Sort by old age") 


    if parameter == "albumL":
         print("Sort by short lenght")

    if parameter == "albumS":
        print("Sort by small lenght") 

    if parameter == "albumC":
        i=0
        dbTotal = 0
        print("print the number of albums in the db")   
        for key in lst.keys():
            while i < len(lst[key]):
               # print(lst[key][i])
                dbTotal += 1
                i += 4
            i = 0 

        return dbTotal
    
    if parameter == "albumG":
        print("Album by genre")

readList()        

