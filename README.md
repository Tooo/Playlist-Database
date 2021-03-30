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
4. In [sqlsetup.py](https://github.com/Tooo/Playlist-Database/blob/main/sqlsetup.py), 
   fill in your MySQL connection settings.
```python
    host = "localhost"
    user = "user"
    password = "password"
    db = "playlistdatabase"
```
5. Run app.py.
```bash
python3 app.py
```
6. Open this URL on your web browser
```bash
localhost:5000
```
