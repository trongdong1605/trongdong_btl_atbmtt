
from flask import Flask, render_template, request
import socket
import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import DES3
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sender.html')

@app.route('/send', methods=['POST'])
def send():
    file = request.files['file']
    file_data = file.read()

    # Tạo khóa RSA và DES3
    private_key = RSA.import_key(open('private.pem').read())
    session_key = get_random_bytes(24)  # DES3 cần 24 byte
    iv = get_random_bytes(8)
    cipher = DES3.new(session_key, DES3.MODE_CBC, iv)
    ciphertext = cipher.encrypt(file_data.ljust((len(file_data) + 7) // 8 * 8))  # Đảm bảo kích thước chia hết cho 8

    # Ký metadata
    metadata = b"legal_doc.txt, timestamp, transaction_id"
    hash_metadata = SHA512.new(metadata)
    signer = pkcs1_15.new(private_key)
    signature = signer.sign(hash_metadata)

    # Tính hash của dữ liệu mã hóa
    hash_value = SHA512.new(iv + ciphertext).hexdigest()

    # Gửi dữ liệu qua socket đến Server 1
    data = {
        'iv': base64.b64encode(iv).decode(),
        'cipher': base64.b64encode(ciphertext).decode(),
        'hash': hash_value,
        'sig': base64.b64encode(signature).decode()
    }

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5001))  # Server 1
    client_socket.send(str(data).encode())
    client_socket.close()

    return 'File sent successfully!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
