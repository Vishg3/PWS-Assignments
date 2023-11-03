from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Change this to a secure secret key
socketio = SocketIO(app)

# Define a simple chat room
chat_room = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    chat_room.append(message)
    emit('message', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
