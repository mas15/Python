import glob
import os
import re
import operator


def most_popular_artists():
    os.chdir("/home/stanek/Music/Disco Polo")
    songs = list()
    artists = dict()
    for file in glob.glob("*.mp3"):
        songs.append(file)
    songs.sort()
    for s in songs:
        name = re.search(r'^.+(?=-)', s).group(0)
        if name in artists:
            artists[name] += 1
        else:
            artists[name] = 1

    sorted_artists = sorted(artists.items(), key=operator.itemgetter(1))
    for a in sorted_artists:
        print(a)


if __name__ == '__main__':
    most_popular_artists()
