from song import *
from playlist import *
from user import *
from relations import *
from sqlsetup import *

def setup():
    sqlsetup = SQLSetup()
    sqlsetup.create_playlist_database()
    sqlsetup.create_all_tables()

def introduction_prints():
    print("** Playlist Database **")
    print("1 - Login")

setup()
introduction_prints()
input1 = input("> ")

if (input1 == "1"):
    username = input("Enter Username: ")
    userManager = UserManager()
    user = userManager.get_user(username)
    if (user == None):
        newUser = User(username)
        print(username + " not found in database. Do you want to create a new user? (y/n)")
        inputCreate = input("> ")
        if (inputCreate == "y"):
            userManager.insert_user(newUser)
            print(username + " has been added to database")
        else:
            print("Bye!")
    else:
        print("Logining to " + user.username)    