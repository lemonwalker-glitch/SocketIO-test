from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'test' #ignore
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('./ChatAppPage.html')

@app.route('/welcome')
def welcome():
    return render_template('./welcome.html')

@socketio.on('my event') #listener, listens from the html file to send something
def handle_my_custom_event(json):
    print('received something: ' + str(json))
    socketio.emit('my response', json )

@socketio.on('my redirect')# this one listens until in the jquery an emit() is sent to my redirect and then this function sends a emit function back calling the redirect in the html
def handle_my_custom_event(json):
    print(str(json))
    #socketio.emit('redirect', {'url': url_for('welcome')})
    redirect()


def redirect():
    socketio.emit('redirect', {'url': url_for('welcome')})
    

if __name__ == '__main__':
    socketio.run(app, debug=True)