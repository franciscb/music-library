import subprocess as sbp


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
filename = 'text_albums_data.txt'
with open('text_albums_data.txt') as fin:
    for line in fin:
        songs.append(line)

for i in range(len(songs)):
    songs[i] = songs[i].rstrip('\n').split(',')


alph = lambda items: time_to_int(items[4])
songs.sort (key = alph)
j = 1
with open("some_text.txt", 'w') as fll:

    for i in range(len(songs)):
        print("{} -{}- -{}- -{}- -{}- -{}-".format(j,songs[i][0], songs[i][1], songs[i][2], songs[i][3], songs[i][4]))
        fll.write("{} -{}- -{}- -{}- -{}- -{}-".format(j,songs[i][0], songs[i][1], songs[i][2], songs[i][3], songs[i][4]) + '\n')
        print('\n')
        j=j+1

sbp.call(['gedit', 'some_text.txt'])

