from flask import *
from sqlsetup import *
from user import *

app = Flask(__name__)
sqlSetup = SQLSetup()
sqlSetup.create_playlist_database()
sqlSetup.create_all_tables()


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if 'delete' in request.form:
            username = request.cookies.get('username')
            userManager = UserManager()
            userManager.delete_user(username)
    return render_template('login.html')


@app.route('/main', methods=['POST', 'GET'])
def main():
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
        genres = userManager.get_user_genre(user)
        resp = make_response(render_template("main.html", message=message, genres=genres))
        resp.set_cookie('username', username)
        return resp


if __name__ == '__main__':
    app.run(debug=True)
