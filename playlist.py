class Playlist:
    def __init__(self, name, username, date):
        self.name = name
        self.username = username
        self.date = date


class PublicPlaylist(Playlist):
    def __init__(self, name, username, date):
        super().__init__(name, username, date)


class PrivatePlaylist(Playlist):
    def __init__(self, name, username, date, password):
        super().__init__(name, username, date)
        self.password = password
