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

songs = list()
filename = 'Albums.txt'
with open('Albums.txt') as fin:
    for line in fin:
        songs.append(line)

print(":              Band name                  :                Song name           :       Year       :         Genre       :     Minutes      : ")

for i in range(len(songs)):
    songs[i] = songs[i].rstrip('\n').split(',')


minutes = lambda items: time_to_int(items[4])
songs.sort (key = minutes)



for items in songs:
    print( ":", items[0] ," "*(38-len(items[0])) ,
           ":", items[1] ," "*(33-len(items[1])) ,
           ":", items[2] ," "*(15-len(items[2])) ,
           ":", items[3] ," "*(18-len(items[3])) ,
           ":", items[4] ," "*(15-len(items[4])) , ":" )



print(type(songs))
