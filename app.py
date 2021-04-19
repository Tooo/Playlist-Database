from time import time

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
    userManager = UserManager()
    playlistManager = PlaylistManager()
    if 'login' in request.form:
        username = request.form['username']
        user = userManager.get_user(username)
        if user is None:
            user = User(username)
            message = username + " has been created"
            userManager.insert_user(user)
        else:
            message = "Hello " + username

    #
    # elif 'userRating' in request.form:
    #     userRating = request.form['userRating']
    else:
        username = request.cookies.get('username')
        user = User(username)
        message = "Hello " + username
    genres = userManager.get_user_genre(user)
    songManager = SongManager()
    songList = songManager.get_songs()

    songList=songManager.get_songs()
    playlists = playlistManager.get_user_playlists(username)
    listofgenres = playlistManager.genre_list(playlists, username)
    popular_songs = songManager.song_in_every_playlist()
    resp = make_response(
        render_template("index.html", message=message, genres=genres, songList=songList, playlists=playlists,
                        genrelists=listofgenres, popular_songs=popular_songs))
    resp.set_cookie('username', username)
    return resp


@app.route('/addSong', methods=['POST'])
def add_song_to_playlist():
    username = request.cookies.get('username')
    addSong = request.form['addSong']
    playlistManager = PlaylistManager()
    playlistManager.insert_song_in_playlist('My Pop List', username, addSong)

    return redirect('home#createplaylist')


@app.route('/createPlaylist', methods=['POST'])
def create_playlist_button():
    username = request.cookies.get('username')
    name = request.form['plName']
    playlistManager = PlaylistManager()
    if not playlistManager.is_playlist_in_user(name, username):
        if request.form['visibility'] == "private":
            password = request.form['plPassword']
            playlistManager.insert_private_playlist(PrivatePlaylist(name, username, time(), password))
        else:
            playlistManager.insert_public_playlist(PublicPlaylist(name, username, time()))
    return redirect('/home#playlist')


@app.route('/viewplaylistlogin', methods=['POST'])
def view_playlist_button():
    username = request.cookies.get('username')
    name = request.form['plName']
    playlistManager = PlaylistManager()
    songManager = SongManager()
    songList=songManager.get_songs()
    if playlistManager.is_private(name,username)==True:
        password = request.form['plPassword']
        if playlistManager.password_check(name,username, password) == True:
            playlistSong = playlistManager.get_songs_in_playlist(name,username)
            resp = make_response(render_template("playlist.html",songList=songList,playlistSong=playlistSong))
            return resp
    else:
        playlistSong = playlistManager.get_songs_in_playlist(name,username)
        resp = make_response(render_template("playlist.html",songList=songList,playlistSong=playlistSong))
        return resp
    return


@app.route('/genreButton', methods=['POST'])
def genre_button():
    username = request.cookies.get('username')
    genre = request.form['genre']
    user = User(username)
    userManager = UserManager()
    if userManager.is_genre_in_user_genre(user, genre):
        userManager.delete_user_genre(user, genre)
    else:
        userManager.insert_user_genre(user, genre)
    return redirect('/home#settings')


@app.route('/deleteUser', methods=['POST'])
def delete_user_button():
    username = request.cookies.get('username')
    userManager = UserManager()
    userManager.delete_user(username)
    return redirect('/')


@app.route('/updateUser', methods=['POST'])
def update_username_button():
    username = request.cookies.get('username')
    userManager = UserManager()
    new_username = request.form['username']
    userManager.update_username(username, new_username)
    return redirect('/')


@app.route('/homeGenre', )
def home_genre():
    userManager = UserManager()
    username = request.cookies.get('username')
    user = User(username)
    genres = userManager.get_user_genre(user)
    return render_template('genre.html', genres=genres)


@app.route('/homePlaylist')
def home_playlist():
    playlistManager = PlaylistManager()
    username = request.cookies.get('username')
    playlists = playlistManager.get_user_playlists(username)
    return render_template('playlist.html', playlists=playlists)


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
