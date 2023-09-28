import sqlite3 


CONN = sqlite3.connect('phase-3/python-p3-v2-final-project-template/snake_scores.db')
c = CONN.cursor()

c.execute("""CREATE TABLE player_name (
          player_name TEXT, 
          score INTEGER,
          id INTEGER
    )""")

all_scores = [
    ("giorgi", 10)
]

c.executemany("INSERT INTO player_name VALUES (?, ?, ?)", all_scores)
c.execute("SELECT * FROM score") 
my_data = c.fetchall()

for i in my_data:
    print(i)

CONN.commit()
CONN.close()

