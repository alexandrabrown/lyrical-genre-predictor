import sqlite3
conn = sqlite3.connect('mxm_dataset.db')
c = conn.cursor()
for row in c.execute('SELECT * FROM Lyrics LIMIT 5'):
        print row