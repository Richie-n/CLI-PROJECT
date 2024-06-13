import sqlite3
CONN = sqlite3.connect('music.db')
CURSOR = CONN.cursor()

class Database:
    def create_tables(self):
        sql1 = '''
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(20) ,
            album VARCHAR(20) ,
            genre VARCHAR(20) 
        );
        '''
        CURSOR.execute(sql1)

        sql2 = '''
        CREATE TABLE IF NOT EXISTS artists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(30),
            genre VARCHAR(20),
            origin VARCHAR(20) 
        );
        '''
        CURSOR.execute(sql2)

        sql3 = '''
        CREATE TABLE IF NOT EXISTS artist_song (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            song_id INTEGER,
            artist_id INTEGER,

            FOREIGN KEY (song_id) REFERENCES songs(id),
            FOREIGN KEY (artist_id) REFERENCES artists(id)
        );
        '''
        CURSOR.execute(sql3)

        sql4 = '''
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            review INTEGER,
            song_id TEXT,
            artist_id TEXT,

            FOREIGN KEY (song_id) REFERENCES songs(id),
            FOREIGN KEY (artist_id) REFERENCES artists(id)
        );
        '''
        CURSOR.execute(sql4)
        CONN.commit() 

    

    def drop_tables(self):
        sql1 = '''
        DROP TABLE IF EXISTS songs;
        '''
        CURSOR.execute(sql1)

        sql2 = '''
        DROP TABLE IF EXISTS artists;
        '''
        CURSOR.execute(sql2)

        sql3 = '''
        DROP TABLE IF EXISTS artist_song;
        '''
        CURSOR.execute(sql3)

        sql4 = '''
        DROP TABLE IF EXISTS reviews;
        '''
        CURSOR.execute(sql4)
        CONN.commit()


db = Database()

# db.drop_tables()
# print('************************TABLES DROPPED!!************************')

# print('._._._._._._._._._._._._CREATING TABLES!!._._._._._._._._._._._.')

# db.create_tables()
# print('*-*-*-*-*-*-*-*-*-*-*-*-4 TABLES CREATED!!!*-*-*-*-*-*-*-*-*-*-*')