from lib.config import CONN, CURSOR

class Artist:
    #CREATING ARTIST
    @classmethod
    def create(cls, name, genre, origin):
        sql = "INSERT INTO artists (name, genre, origin) VALUES (?, ?, ?)"
        CURSOR.execute(sql, (name, genre, origin))
        CONN.commit()

        return CURSOR.lastrowid 
    
    #FETCHING ARTIST
    @classmethod
    def fetch_artist(cls, id):
        sql = "SELECT * FROM artists WHERE id = ?"
        CURSOR.execute(sql, (id, ))
        return CURSOR.fetchone()

    # UPDATING ARTIST
    @classmethod
    def update_artist(cls, id, name, genre, origin):
        sql = "UPDATE artists SET name = ?, genre = ?, origin = ? WHERE id = ?"
        CURSOR.execute(sql, (name, genre, origin, id))
        CONN.commit()
        return "Artist updated successfully"
    
    #DELETING ARTIST
    @classmethod
    def delete_artist(cls, id):
        sql = "DELETE FROM artists WHERE id = ?"
        CURSOR.execute(sql, (id, ))
        CONN.commit()
        return "Artist deleted successfully"
    
    #FETCHING ALL ARTIST
    @classmethod
    def fetch_all_artists(cls):
        sql = "SELECT * FROM artists"
        CURSOR.execute(sql)
        return CURSOR.fetchall()

    #TOTAL ARTISTS
    @classmethod
    def total_artists(cls):
        sql = "SELECT COUNT(*) FROM artists"
        CURSOR.execute(sql)
        return CURSOR.fetchone()