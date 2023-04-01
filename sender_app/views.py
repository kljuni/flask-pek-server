from datetime import datetime
from flask import Blueprint, jsonify, request, render_template
from flask_socketio import SocketIO, emit

socketio = SocketIO()
blueprint = Blueprint('user', __name__)

saved_string = ""
saved_date_and_time = ""


@blueprint.route('/api/save', methods=['POST'])
def save_string():
    global saved_string
    global saved_date_and_time
    saved_string = request.json
    saved_date_and_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    socketio.emit('update', {'saved_string': saved_string, 'saved_date_and_time': saved_date_and_time})
    return jsonify({'message': 'String saved successfully!'}), 200

@blueprint.route('/')
def display_string():
    global saved_string
    global saved_date_and_time
    return render_template('display_string.html', saved_string=saved_string, saved_date_and_time=saved_date_and_time)

@socketio.on('connect')
def on_connect():
    emit('update', {'saved_string': saved_string, 'saved_date_and_time': saved_date_and_time})