import sqlite3
conn = sqlite3.connect('mxm_dataset.db')


# Retrieves the track from the database by id
def get_track(track_id):
    c = conn.cursor()
    c.execute('SELECT word, count FROM Lyrics WHERE track_id="%s"' % track_id)
    words = c.fetchall()
    c.close()

    lyrics = []
    for word, count in words:
        lyrics.extend([word for i in range(count)])
    return " ".join(lyrics)


# Returns a list of tracks from the database given ids
def get_track_list(track_ids):
    return [get_track(id) for id in track_ids]


# Returns if the track has lyrics associated with it
def track_has_lyrics(track_id):
    c = conn.cursor()
    c.execute('SELECT word FROM Lyrics WHERE track_id="%s"' % track_id)
    return (len(c.fetchall()) != 0)


def word_present(word):
    c = conn.cursor()
    c.execute('SELECT * from Words where word = "%s"' % word)
    return (len(c.fetchall()) != 0)
