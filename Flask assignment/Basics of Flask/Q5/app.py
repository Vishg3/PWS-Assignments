from flask import Flask, request, render_template, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)

# Configure the app to use the "filesystem" session type
app.config['SESSION_TYPE'] = 'filesystem'

# Initialize the session extension
Session(app)

# Secret key for session management. You should set a random secret key in a real app.
app.secret_key = 'your_secret_key'

# A dictionary to simulate user-specific data
user_data = {}

@app.route('/')
def index():
    # Check if the user is logged in (their username is stored in the session)
    if 'username' in session:
        username = session['username']
        user_info = user_data.get(username, "No user data available.")
        return f'Hello, {username}! User Data: {user_info}<br><a href="/logout">Logout</a>'
    else:
        return 'You are not logged in.<br><a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        # Simulate user authentication
        if username == 'user1':
            # Store the username in the session
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Login failed. Please try again.'

    return render_template('login.html')

@app.route('/logout')
def logout():
    # Remove the username from the session if it exists
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host= "0.0.0.0" , port = 5002)
