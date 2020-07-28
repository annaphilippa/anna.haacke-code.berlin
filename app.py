from flask import Flask, redirect, render_template, request, session, url_for
import os
import sqlite3 as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tO8U0V8ZVcVn6tAOT5I3dCgNqTaiJ5Y0yO16trmy8i5PAyzsJi'

@app.route('/')
def home():
    if 'username' in session:
        username = session['username']
        return render_template('home.html')
        
    else:
        return render_template('login.html', text="Please Login to see my Gallery")

    


@app.route('/faces')
def faces():
    if 'username' in session:
        username = session['username']
        images = os.listdir(os.path.join(app.static_folder, "images/faces"))
        return render_template('facesproject.html', images=images)
    else:
        return render_template('login.html' , text="Please Login to see my Gallery")

@app.route('/ears')
def ears():
    if 'username' in session:
        username = session['username']
        images = os.listdir(os.path.join(app.static_folder, "images/ears"))
        return render_template('earsproject.html', images=images)
    else:
        return render_template('login.html', text="Please Login to see my Gallery")


@app.route('/hands')
def hands():
    if 'username' in session:
        username = session['username']
        images = os.listdir(os.path.join(app.static_folder, "images/hands"))
        return render_template('handsproject.html', images=images)
    else:
        return render_template('login.html', text="Please Login to see my Gallery")


@app.route('/objects')
def objects():
    if 'username' in session:
        username = session['username']
        images = os.listdir(os.path.join(app.static_folder, "images/objects"))
        return render_template('objectsproject.html', images=images)
    else:
        return render_template('login.html', text="Please Login to see my Gallery")


@app.route('/donate')
def donate():
    return render_template('donate.html')



@app.route('/login', methods=["GET","POST"])
def do_admin_login():
    if request.method == "POST":

        POST_USERNAME = request.form['username']
        POST_PASSWORD = request.form['password']

        con = sql.connect("users.db")
        cursor = con.cursor()

        query = f"SELECT username FROM users WHERE username='{POST_USERNAME}' and password='{POST_PASSWORD}'"
        cursor.execute(query)
        user = cursor.fetchone()

        if user is not None:
            session['username'] = user[0]
            return redirect(url_for('home'))
        else: 
            return render_template('login.html', text="Username or Password wrong! Please try again.")


    else:
        return render_template('login.html',text="Please Login to see my Gallery")


@app.route("/logout")
def logout():
    session.pop('username', None)
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)
