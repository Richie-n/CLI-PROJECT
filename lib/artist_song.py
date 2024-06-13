from lib.config import CONN, CURSOR

class ArtistSong:
    
    @classmethod
    def create(cls, song_id, artist_id):
        sql = "INSERT INTO artist_song (song_id, artist_id) VALUES (?, ?)"
        CURSOR.execute(sql, (song_id, artist_id))
        CONN.commit()
        return CURSOR.lastrowid
    

    
    # FETCHING ARTISTS ASSOCIATED WITH A SONG
    @classmethod
    def fetch_artists_by_song_id(cls, song_id):
        sql = '''
        SELECT artists.name
        FROM artists
        INNER JOIN artist_song
        ON artists.id = artist_song.artist_id
        WHERE artist_song.song_id = ? '''
        CURSOR.execute(sql, (song_id, ))
        return CURSOR.fetchall()


    
    # FETCHING SONGS ASSOCIATED WITH AN ARTIST
    @classmethod
    def fetch_songs_by_artist_id(cls, artist_id):
        sql = '''SELECT songs.name
        FROM songs
        INNER JOIN artist_song 
        ON songs.id = artist_song.song_id
        WHERE artist_song.artist_id = ? '''
        CURSOR.execute(sql, (artist_id, ))
        return CURSOR.fetchall()