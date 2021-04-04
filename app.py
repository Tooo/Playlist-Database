from flask import *

from model.playlist import *
from model.song import *
from model.user import *

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        if 'delete' in request.form:
            username = request.cookies.get('username')
            userManager = UserManager()
            userManager.delete_user(username)
    return render_template('login.html')


@app.route('/home', methods=['POST', 'GET'])
def home_page():
    if request.method == 'POST':
        userManager = UserManager()
        if 'login' in request.form:
            username = request.form['username']
            user = userManager.get_user(username)
            if user is None:
                user = User(username)
                message = username + " has been created"
                userManager.insert_user(user)
            else:
                message = "Hello " + username
        elif 'genreButton' in request.form:
            username = request.cookies.get('username')
            genre = request.form['genre']
            user = User(username)
            if userManager.is_genre_in_user_genre(user, genre):
                userManager.delete_user_genre(user, genre)
            else:
                userManager.insert_user_genre(user, genre)
            message = "Hello " + username
        else:
            username = request.cookies.get('username')
            user = User(username)
            message = "Hello " + username
        genres = userManager.get_user_genre(user)
        resp = make_response(render_template("index.html", message=message, genres=genres))
        resp.set_cookie('username', username)
        return resp


@app.route('/homeGenre', )
def home_genre():
    userManager = UserManager()
    username = request.cookies.get('username')
    user = User(username)
    genres = userManager.get_user_genre(user)
    return render_template('pl1.html', genres=genres)


@app.route('/homePlaylist')
def home_playlist():
    playlistManager = PlaylistManager()
    username = request.cookies.get('username')
    playlists = playlistManager.get_user_playlists(username)
    return render_template('pl2.html', playlists=playlists)


@app.route('/playlist', methods=['POST', 'GET'])
def playlist_page():
    if request.method == 'POST':
        username = request.cookies.get('username')
        playlistManager = PlaylistManager()
        if 'playlistButton' in request.form:
            playlistName = request.form['playlist']
            if playlistManager.is_playlist_in_user(playlistName, username):
                playlistManager.delete_playlist(playlistName, username)
            else:
                playlist = Playlist(playlistName, username, 0)
                playlistManager.insert_playlist(playlist)
        playlists = playlistManager.get_user_playlists(username)
        resp = make_response(render_template("index.html", playlists=playlists))
        return resp


@app.route('/songs', methods=['POST', 'GET'])
def songs_page():
    songManager = SongManager()
    songList = songManager.get_songs()
    resp = make_response(render_template("index.html", songList=songList))
    return resp


@app.route('/settings', methods=['POST', 'GET'])
def settings_page():
    if request.method == 'POST':
        userManager = UserManager()
        username = request.cookies.get('username')
        user = User(username)
        if 'genreButton' in request.form:
            genre = request.form['genre']
            if userManager.is_genre_in_user_genre(user, genre):
                userManager.delete_user_genre(user, genre)
            else:
                userManager.insert_user_genre(user, genre)
        genres = userManager.get_user_genre(user)
        resp = make_response(render_template("settings.html", genres=genres))
        return resp


if __name__ == '__main__':
    app.run(debug=True)
