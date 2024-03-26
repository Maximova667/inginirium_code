import sqlite3


class DataBase:
    def __init__(self, file):
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
        self.create_table('score')

    def create_table(self, table_name):
        que = f'''CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            score_point INTEGER
        )
        '''
        self.cur.execute(que)
        self.con.commit()

    def get(self, gue='SELECT * FROM score ORDER BY score_point DESC'):
        return self.cur.execute(gue).fetchall()

    def insert(self, name, score):
        gue = f'''INSERT INTO score (name, score_point) VALUES ('{name}', {score})'''
        self.cur.execute(gue)
        self.con.commit()

    def __del__(self):
        self.con.close()


db = DataBase('score.sglite3')
# db.insert('Tor', 20)
# db.insert('Loki', 15)
# db.insert('Tony', 17)
list = db.get()
for i in list:
    print(i)
