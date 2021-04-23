# Playlist Database
A database that holds a list of songs and playlists from users.
Users will choose their song genres and create a playlist of songs.
They can create public playlists or share their private playlists.
Other users can rate the private playlist.

## Installation
1. Download and install [Python 3.9.](https://www.python.org/downloads/release/python-392/)
2. Install required python packages.
```bash
pip install -r requirement.txt
```
3. Set up a MySQL database with [mySQL Installer](https://dev.mysql.com/downloads/installer/)
   and [mySQL workbench.](https://dev.mysql.com/downloads/workbench/)
4. In [config.py](https://github.com/Tooo/Playlist-Database/blob/main/config.py), 
   fill in your MySQL connection settings.
```python
DB_HOST = 'localhost'
DB_USER = 'user'
DB_PASSWORD = 'password'
DB_DATABASE = 'playlistdatabase'
```
5. Run sqlsetup.py to set up the database and import all the songs.
```bash
python3 sqlsetup.py
```
5. Run app.py.
```bash
python3 app.py
```
6. Open this URL on your web browser
```bash
localhost:5000
```

## Features
- Save your genres and playlists in your own account.
- Create public or private playlists with passwords.
- Add from 300 songs from our song database.
- Rate each song, either upvoting or downvoting


## Demos
### Implementation Demo
https://www.youtube.com/watch?v=SFK4WphyL1c

### Application Demo
https://www.youtube.com/watch?v=O42S7y5rHyQ

## Planning 
### ER Diagram
![ER](https://github.com/Tooo/Playlist-Database/blob/main/static/images/ERdiagram.png)

### Database Schema
#### Relations
Song [<ins>SongID</ins>, Name, Duration, Artist, Genre] <br/>
User [<ins>Username</ins>] <br/>
Playlist [<ins>Name, Username</ins>, Date] <br/>
Public [<ins>Name, Username</ins>] <br/>
Private [<ins>Name, Username</ins>, Password] <br/>
Rate [<ins>Username, SongID</ins>, Rating] <br/>
Contains [<ins>SongID, Name</ins>] <br/>
Share [<ins>Username, Name, SuperUsername</ins>, Rating, Comment] <br/>
UserGenres [<ins>Username, Genres</ins>]

#### Foreign Keys
Playlist.Username references User.Username <br/>
Public.Name references Playlist.Name <br/>
Public.Username references User.Username <br/>
Private.Name references Playlist.Name <br/>
Private.Username references User.Username <br/>
Rate.Username references User.Username <br/>
Rate.SongID references Song.SongID <br/>
Contains.SongID references Song.SongID <br/>
Contains.Name references Playlist.Name <br/>
Share.Username references User.Username <br/>
Share.SuperUsername references User.Username <br/>
Share.Name references Playlist.Name <br/>
UserGenres.Username references User.Username<br/>

