import mysql.connector


class SQLSetup:
    host = "localhost"
    user = "user"
    password = "password"
    db = "playlistdatabase"

    def create_playlist_database(self):
        db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        c = db.cursor()
        c.execute("CREATE DATABASE IF NOT EXISTS playlistdatabase")
        c.close()
        db.close()

    def create_all_tables(self):
        db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.db
        )
        self.create_song_table(db)
        self.create_user_table(db)
        self.create_playlist_table(db)
        self.create_public_playlist_table(db)
        self.create_private_playlist_table(db)
        self.create_rate_table(db)
        self.create_contains_table(db)
        self.create_share_table(db)
        self.create_user_genre_table(db)
        self.create_song_genre_table(db)
        db.close()

    def create_song_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Song (
                        songID INTEGER, 
                        name VARCHAR(255), 
                        duration INTEGER, 
                        artist VARCHAR(255), 
                        PRIMARY KEY (songID)
        )""")
        c.close()

    def create_user_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS User (
                        username VARCHAR(255), 
                        PRIMARY KEY (username)
        )""")
        c.close()

    def create_playlist_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Playlist (
                        name VARCHAR(255),
                        username VARCHAR(255),
                        date VARCHAR(255),
                        PRIMARY KEY(name, username),
                        FOREIGN KEY (username) REFERENCES User (username)
        )""")
        c.close()

    def create_public_playlist_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Public (
                        name VARCHAR(255),
                        username VARCHAR(255),
                        PRIMARY KEY(name, username),
                        FOREIGN KEY (username) REFERENCES Playlist (username)
        )""")
        c.close()

    def create_private_playlist_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Private (
                        name VARCHAR(255),
                        username VARCHAR(255),
                        password VARCHAR(255),
                        PRIMARY KEY(name, username),
                        FOREIGN KEY (username) REFERENCES Playlist (username)
        )""")
        c.close()

    def create_rate_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Rate (
                        username VARCHAR(255),
                        songID INTEGER,
                        Rating BOOLEAN, 
                        PRIMARY KEY (username, songID),
                        FOREIGN KEY (username) REFERENCES User (username),
                        FOREIGN KEY (songID) REFERENCES Song (songID)
        )""")
        c.close()

    def create_contains_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Contains ( 
                        name VARCHAR(255), 
                        username VARCHAR(255),
                        songID INTEGER,
                        PRIMARY KEY (name, username, songID),
                        FOREIGN KEY (songID) REFERENCES Song (songID),
                        FOREIGN KEY (name) REFERENCES Playlist (name),
                        FOREIGN KEY (username) REFERENCES User (username)
        )""")
        c.close()

    def create_share_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Share (
                        username VARCHAR(255), 
                        name VARCHAR(255), 
                        superUsername VARCHAR(255),
                        rating BOOLEAN,
                        comment VARCHAR(255), 
                        PRIMARY KEY (username, name, superusername),
                        FOREIGN KEY (username) REFERENCES User (username),
                        FOREIGN KEY (name) REFERENCES Playlist (name),
                        FOREIGN KEY (superUsername) REFERENCES User (username)
        )""")
        c.close()

    def create_user_genre_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS UserGenre (
                        username VARCHAR(255), 
                        genre VARCHAR(255), 
                        PRIMARY KEY (username, genre),
                        FOREIGN KEY (username) REFERENCES User (username)
        )""")
        c.close()

    def create_song_genre_table(self, db):
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS SongGenre (
                        songID INTEGER, 
                        genre VARCHAR(255), 
                        PRIMARY KEY (songID, genre),
                        FOREIGN KEY (songID) REFERENCES Song (songID)
        )""")
        c.close()
