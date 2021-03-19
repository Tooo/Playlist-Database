from flask import *
from sqlsetup import *
from user import *

app = Flask(__name__)
sqlSetup = SQLSetup()
sqlSetup.create_playlist_database()
sqlSetup.create_all_tables()


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/main', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        username = request.form['username']
        userManager = UserManager()
        user = userManager.get_user(username)
        if user is None:
            newUser = User(username)
            message = username + " has been created"
            userManager.insert_user(newUser)
        else:
            message = "Hello " + username
        return render_template("main.html", message=message)


if __name__ == '__main__':
    app.run()
