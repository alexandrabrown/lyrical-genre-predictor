import sqlite3
conn = sqlite3.connect('mxm_dataset.db')


def get_track(track_id):
    c = conn.cursor()
    c.execute('SELECT word, count FROM Lyrics WHERE track_id="%s"' % track_id)
    words = c.fetchall()
    c.close()

    lyrics = []
    for word, count in words:
        lyrics.extend([word for i in range(count)])
    return " ".join(lyrics)


def get_track_list(track_ids):
    return [get_track(id) for id in track_ids]


def track_has_lyrics(track_id):
    c = conn.cursor()
    c.execute('SELECT word FROM Lyrics WHERE track_id="%s"' % track_id)
    return c.rowcount != -1
