from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'test'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('./ChatAppPage.html')

@app.route('/welcome')
def welcome():
    return render_template('./welcome.html')

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received something: ' + str(json))
    socketio.emit('my response', json )

@socketio.on('my redirect')
def handle_my_custom_event(json):
    print(str(json))
    socketio.emit('redirect', {'url': url_for('welcome')})

if __name__ == '__main__':
    socketio.run(app, debug=True)