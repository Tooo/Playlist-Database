from model.song import *
from model.user import *
from model.playlist import *

def introduction_prints():
    print("** Playlist Database **")
    print("1 - Login")


introduction_prints()
input1 = input("> ")

if input1 == "1":
    username = input("Enter Username: ")
    userManager = UserManager()
    user = userManager.get_user(username)
    songManager = SongManager()
    playlistManager = PlaylistManager()
    if user is None:
        newUser = User(username)
        print(username + " not found in database. Do you want to create a new user? (y/n)")
        inputCreate = input("> ")
        if inputCreate == "y":
            userManager.insert_user(newUser)
            print(username + " has been added to database")
        else:
            print("Bye!")
    else:
        print("Logging to " + user.username)
    user = userManager.get_user(username)
    command = input("Enter a command: (insert/delete)")
    if command == "delete":
        command = input("Delete genre or user?: (genre/user)")
        if command == "user":
            userManager.delete_user(user.username)
        elif command == "genre":
            command = input("Genre to be deleted:")
            userManager.delete_user_genre(user, command)
    elif command == "insert":
        command = input("playlist to be inserted:")
        #song = Song(123, 'music', 'pop', 'Cheng', '12:02')
        #songManager.insert_song(song)
        newlist = Playlist("list","Andrew","12312")
        playlistManager.insert_playlist(newlist)
    elif command == "p":
        command = input("Password:")
        playlistManager.make_private("list","Andrew",command)
    elif command  == "pub":
        command = input("Password:")
        if playlistManager.password_check("list","Andrew",command) == True:
            playlistManager.make_public("list","Andrew")
        else:
            print("Wrong password!")