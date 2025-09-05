from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret' # a secret key for security
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True) # Broadcast the message to all clients

if __name__ == '__main__':
    socketio.run(app, debug=True)