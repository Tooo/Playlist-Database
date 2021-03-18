import mysql.connector

class SQLSetup:
    def create_playlist_database(self):
        db = mysql.connector.connect(
            host = "localhost",
            user = "user",
            password = "password"
        )
        c = db.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS playlistdatabase")
        c.close()
        db.close()
    
    def create_song_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS song (
                        songID INTEGER, 
                        name VARCHAR(255), 
                        duration INTEGER, 
                        artist VARCHAR(255), 
                        PRIMARY KEY (songID)
        )""")
        c.close()

    def create_all_tables(self):
        db = mysql.connector.connect(
            host = "localhost",
            user = "user",
            password = "password",
            database = "playlistdatabase"
        )
        self.create_song_table(db)
        # create_user_table(db)
        # create_playlist_table(db)
        # create_public_playlist_table(db)
        # create_private_playlist_table(db)
        # create_rate_table(db)
        # create_contains_table(db)
        # create_share_table(db)
        # create_user_genre_table(db)
        # create_song_genre_table(db)
        db.close()

    