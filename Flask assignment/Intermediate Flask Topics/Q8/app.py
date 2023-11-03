from flask import Flask, request, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your own secret key
login_manager = LoginManager()
login_manager.init_app(app)

# In-memory user storage (replace with a database)
users = {
    1: User(1, 'user1', 'password1'),
    2: User(2, 'user2', 'password2')
}

class User(UserMixin):
    def __init__(self, user_id, username, password):
        self.id = user_id
        self.username = username
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = next((user for user in users.values() if user.username == username and user.password == password), None)
        if user:
            login_user(user)
            return redirect(url_for('protected'))
    return render_template('login.html')

@app.route('/protected')
@login_required
def protected():
    return 'You are logged in as: ' + current_user.username

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_id = len(users) + 1  # Generate a unique user_id
        user = User(user_id, username, password)
        users[user_id] = user
        login_user(user)
        return redirect(url_for('protected'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
