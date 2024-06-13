from lib.config import CONN, CURSOR

class Songs:
    #CREATING SONG
    @classmethod
    def create_song(cls, name, album, genre):
        sql = "INSERT INTO songs (name, album, genre) VALUES (?, ?, ?)"
        CURSOR.execute(sql, (name, album, genre))
        CONN.commit()
        return CURSOR.lastrowid
    

    #UPDATING SONG
    @classmethod
    def update_song(cls, id, name, album, genre):
        sql = "UPDATE songs SET name = ?, album = ?, genre = ? WHERE id = ?"
        CURSOR.execute(sql, (name, album, genre, id))
        CONN.commit()
        return "Song updated successfully"
    
    #DELETING SONG
    @classmethod  
    def delete_song(cls, id):
        sql = "DELETE FROM songs WHERE id = ?"
        CURSOR.execute(sql, (id, ))
        CONN.commit()
        return "Song deleted successfully"

    #FETCHING SONG

    @classmethod
    def fetch_song(cls, id):
        sql = "SELECT * FROM songs WHERE id = ?"
        CURSOR.execute(sql, (id, ))
        return CURSOR.fetchone()

    #FETCHING ALL SONGS

    @classmethod
    def fetch_all_songs(cls):
        sql = "SELECT * FROM songs"
        CURSOR.execute(sql)
        return CURSOR.fetchall()
    
    #TOTAL SONGS

    @classmethod
    def total_songs(cls):
        sql = "SELECT COUNT(*) FROM songs"
        CURSOR.execute(sql)
        return CURSOR.fetchone()

