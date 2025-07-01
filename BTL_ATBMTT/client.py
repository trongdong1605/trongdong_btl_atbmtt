import base64
import rsa
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from hashlib import sha512
from flask_socketio import SocketIO

# Kết nối WebSocket với server Flask
from socketio import Client

socket = Client()

# Kết nối đến Flask server tại địa chỉ localhost và cổng 5000
socket.connect('http://127.0.0.1:5000')

# Gửi thông điệp đến server
def send_message(message):
    socket.emit('message', message)

# Gửi tệp đến server
def send_file(file_path, session_key):
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Tạo IV cho DES
    iv = get_random_bytes(8)

    # Mã hóa tệp bằng DES
    cipher = DES.new(session_key, DES.MODE_CBC, iv)
    padded_data = file_data + b'\x00' * (8 - len(file_data) % 8)
    ciphertext = cipher.encrypt(padded_data)

    # Tính hash SHA-512 của IV + ciphertext
    hash_value = sha512(iv + ciphertext).hexdigest()

    # Mã hóa dữ liệu và chữ ký dưới dạng Base64
    iv_base64 = base64.b64encode(iv).decode()
    cipher_base64 = base64.b64encode(ciphertext).decode()

    # Gửi gói tin (bao gồm IV, ciphertext, hash và tên tệp)
    packet = {
        'iv': iv_base64,
        'cipher': cipher_base64,
        'hash': hash_value,
        'file_name': file_path.split('/')[-1]  # Chỉ lấy tên tệp
    }

    socket.emit('file', packet)
    print("Tệp đã được gửi.")

# Gửi tin nhắn và tệp
send_message("Hello, Server!")
send_file('legal_doc.txt', b"thisisaverysecret")  # Giả sử khóa phiên
