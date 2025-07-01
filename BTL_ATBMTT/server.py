import socket
from datetime import datetime

# Lưu log thời gian giao dịch
def log_transaction(action):
    with open('transaction_log.log', 'a', encoding='utf-8') as log_file:
        log_file.write(f"{datetime.now()} - {action}\n")

# Tạo socket TCP cho Server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 65433))
server_socket.listen(1)
print("Server đang lắng nghe trên 127.0.0.1:65433...")

# Chờ kết nối từ client
client_socket, client_address = server_socket.accept()
print(f"Đã kết nối với {client_address}")

# Nhận tệp tin từ client
file_data = client_socket.recv(1024)
with open('received_file.txt', 'wb') as file:
    file.write(file_data)
log_transaction(f"Nhận tệp từ {client_address}")

client_socket.close()
server_socket.close()
