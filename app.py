from flask import *
from sqlsetup import *
from user import *

app = Flask(__name__)
sqlsetup = SQLSetup()
sqlsetup.create_playlist_database()
sqlsetup.create_all_tables()

@app.route('/')
def login():
   return render_template('login.html')

@app.route('/main', methods = ['POST', 'GET'])
def main():
    if request.method == 'POST':
        username = request.form['username']
        userManager = UserManager()
        user = userManager.get_user(username)
        if (user == None):
            newUser = User(username)
            message = username + " has been created"
            userManager.insert_user(newUser)
        else:
            message = "Hello " + username
        result = request.form
        return render_template("main.html", message = message)

if __name__ == '__main__':
    app.run()