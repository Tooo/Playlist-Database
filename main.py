from song import *
from playlist import *
from user import *
from relations import *
from sqlsetup import *


def setup():
    sqlSetup = SQLSetup()
    sqlSetup.create_playlist_database()
    sqlSetup.create_all_tables()


def introduction_prints():
    print("** Playlist Database **")
    print("1 - Login")


setup()
introduction_prints()
input1 = input("> ")

if input1 == "1":
    username = input("Enter Username: ")
    userManager = UserManager()
    user = userManager.get_user(username)
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
        command = input("Genre to be inserted:")
        userManager.insert_user_genre(user, command)
