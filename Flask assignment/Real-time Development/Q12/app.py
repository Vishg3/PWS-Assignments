from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('update_data')
def handle_update_data(data):
    # You can process and update your data here
    # For example, you can emit the updated data to all connected clients.
    emit('data_updated', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
