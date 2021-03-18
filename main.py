from song import *
from playlist import *
from user import *
from relations import *
import mysql.connector

def introduction_prints():
    print("** Playlist Database **")
    print("1 - Login")

db = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS playlistdatabase")

mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="password",
    database="playlistdatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS user (username VARCHAR(255))")
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

introduction_prints()

input1 = input("> ")

if (input1 == "1"):
    username = input("Enter Username: ")
    user = User(username)
    print(user.username + " has been created.")