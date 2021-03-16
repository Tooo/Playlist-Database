from song import *
from playlist import *
from user import *
from relations import *

def introduction_prints():
    print("** Playlist Database **")
    print("1 - Login")

introduction_prints()

input1 = input("> ")

if (input1 == "1"):
    username = input("Enter Username: ")
    user = User(username)
    print(user.username + " has been created.")