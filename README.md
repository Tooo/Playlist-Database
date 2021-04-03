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
