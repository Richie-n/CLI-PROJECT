from lib.config import CONN, CURSOR

class Reviews:
    # CREATE REVIEWS
    @classmethod
    def create_review(cls, review, song_id, artist_id):
        sql = "INSERT INTO reviews (review, song_id, artist_id) VALUES (?, ?, ?)"
        CURSOR.execute(sql, (review, song_id, artist_id))
        CONN.commit()
        return CURSOR.lastrowid

    # FETCH REVIEWS BY ARTIST ID
    @classmethod
    def fetch_reviews_by_artist_id(cls, artist_id):
        sql = "SELECT * FROM reviews WHERE artist_id = ?"
        CURSOR.execute(sql, (artist_id, ))
        return CURSOR.fetchall()
    
    # FETCH REVIEWS BY SONG ID
    @classmethod
    def fetch_reviews_by_song_id(cls, song_id):
        sql = "SELECT * FROM reviews WHERE song_id = ?"
        CURSOR.execute(sql, (song_id, ))
        return CURSOR.fetchall()
    
    # FETCH ALL REVIEWS
    @classmethod
    def fetch_all_reviews(cls):
        sql = "SELECT * FROM reviews"
        CURSOR.execute(sql)
        return CURSOR.fetchall()
    
    #UPDATE REVIEWS
    @classmethod
    def update_review(cls, id, review, song_id, artist_id):
        sql = "UPDATE reviews SET review = ?  WHERE id = ? AND song_id = ? AND artist_id = ?"
        CURSOR.execute(sql, (review, id, song_id, artist_id))
        CONN.commit()
        return "Review updated successfully"
    
    #DELETE REVIEWS
    @classmethod
    def delete_review(cls, id):
        sql = "DELETE FROM reviews WHERE id = ?"
        CURSOR.execute(sql, (id, ))
        CONN.commit()
        return "Review deleted successfully"
    
    # TOTAL REVIEWS
    @classmethod
    def total_reviews(cls):
        sql = "SELECT COUNT(*) FROM reviews"
        CURSOR.execute(sql)
        return CURSOR.fetchone()
    