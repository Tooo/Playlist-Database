class Song:
    genres = []

    def __init__(self, songID, name, artist, duration):
        self.songID = songID
        self.name = name
        self.artist = artist
        self.duration = duration


class SongGenre:
    def __init__(self, songID, genre):
        self.songID = songID
        self.genre = genre
