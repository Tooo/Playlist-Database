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
    user = User(username)
    print(user.username + " has been created.")