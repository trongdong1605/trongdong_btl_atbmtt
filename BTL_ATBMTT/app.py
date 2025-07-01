from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit
import os
import base64

app = Flask(__name__)
socketio = SocketIO(app)

# Lưu tệp vào thư mục uploads
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

# Cung cấp tệp từ thư mục uploads
@app.route('/uploads/<filename>')
def upload_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# Lắng nghe các sự kiện WebSocket
@socketio.on('message')
def handle_message(message):
    print(f"Nhận tin nhắn: {message}")
    emit('message', message, broadcast=True)

@socketio.on('file')
def handle_file(data):
    try:
        file_data = base64.b64decode(data['file'])  # Giải mã base64 tệp
        file_name = data['fileName']
        
        # Lưu tệp vào thư mục uploads
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        with open(file_path, 'wb') as f:
            f.write(file_data)
        
        print(f"Tệp {file_name} đã được lưu tại {file_path}.")
        
        # Gửi lại thông báo tệp đã được nhận
        emit('file_received', {'fileName': file_name}, broadcast=True)
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        emit('file_received', {'error': str(e)}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
