class User:
    genres = []

    def __init__(self, username):
        self.username = username

class UserGenre:
    def __init__(self, username, genre):
        self.username = username
        self.genre = genre