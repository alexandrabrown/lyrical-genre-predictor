from database import *
import sys

categories = ["Pop", "Rock", "Country", "Blues", "Rap"]
tracks = set()
genres = {}
titles = {}
with open('msd_tagtraum_cd2c.cls') as f:
    for line in f:
        if "#" in line:
            continue
        track, category = line.strip().split(None, 1)
        if category not in categories:
            continue
        if track_has_lyrics(track):
            tracks.add(track)
            genres[track] = category

with open('mxm_779k_matches.txt') as f:
    for line in f:
        if "#" in line:
            continue
        try:
            trackid, artist, title, junk = line.strip().split("<SEP>", 3)
        except ValueError:
            print(line)
            sys.exit()
        if trackid in tracks:
            titles[trackid] = "%s; %s" % (title, artist)

with open("songs_input.txt", "w") as f:
    for track in tracks:
        f.write("%s<sep>%s<sep>%s\n" %
                (track, genres[track], titles.get(track, "NOINFOFOUND")))
