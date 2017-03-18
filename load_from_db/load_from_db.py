import sqlite3
conn = sqlite3.connect('mxm_dataset.db')
c = conn.cursor()
c.execute('SELECT * FROM Lyrics LIMIT 5')
