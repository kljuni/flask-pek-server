from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit
from flask import jsonify
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

saved_string = ""
saved_date_and_time = ""

@app.route('/api/save', methods=['POST'])
def save_string():
    global saved_string
    global saved_date_and_time
    saved_string = request.json
    saved_date_and_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    socketio.emit('update', {'saved_string': saved_string, 'saved_date_and_time': saved_date_and_time})
    return jsonify({'message': 'String saved successfully!'}), 200

@app.route('/')
def display_string():
    global saved_string
    global saved_date_and_time
    return render_template('display_string.html', saved_string=saved_string, saved_date_and_time=saved_date_and_time)

@socketio.on('connect')
def on_connect():
    emit('update', {'saved_string': saved_string, 'saved_date_and_time': saved_date_and_time})

if __name__ == '__main__':
    socketio.run(app)
