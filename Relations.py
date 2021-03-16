class Rate:
    def __init__(self, username, songID, rating):
        self.username = username
        self.songID = songID
        self.rating = rating

class Contains:
    def __init__(self, songID, name):
        self.songID = songID
        self.name = name

class Share:
    def __init__(self, username, name, superUsername, rating, comment):
        self.username = username
        self.name = name
        self.superUsername = superUsername
        self.rating = rating
        self.comment = comment

