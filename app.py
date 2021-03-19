from flask import *
app = Flask(__name__)

@app.route('/')
def login():
   return render_template('login.html')

@app.route('/main', methods = ['POST', 'GET'])
def main():
    if request.method == 'POST':
        result = request.form
        return render_template("main.html", result = result)

if __name__ == '__main__':
    app.run()