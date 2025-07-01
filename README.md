- Giới Thiệu

Dự án này là một hệ thống cho phép người dùng gửi tin nhắn và tệp tin qua giao thức WebSocket và TCP. Hệ thống này được xây dựng với mục tiêu cung cấp một phương thức giao tiếp an toàn, sử dụng các thuật toán mã hóa để bảo vệ dữ liệu trước khi gửi đi. Với khả năng gửi tin nhắn và tệp tin theo thời gian thực, dự án này sử dụng Flask cho backend và Flask-SocketIO cho WebSocket, cùng với các thuật toán mã hóa như DES3 và RSA.
- Chức Năng Cơ Bản

Gửi Tin Nhắn: Người dùng có thể gửi tin nhắn qua WebSocket, nhận tin nhắn ngay lập tức từ máy chủ.

Gửi Tệp Tin: Cho phép người dùng gửi tệp tin qua WebSocket, đồng thời mã hóa tệp tin trước khi gửi để bảo vệ dữ liệu.

Mã Hóa và Chữ Ký: Tệp tin được mã hóa bằng DES3 (Triple DES) và chữ ký RSA được áp dụng để đảm bảo tính bảo mật của tệp tin và dữ liệu.

Lưu Trữ và Truy Cập Tệp: Các tệp tin gửi qua WebSocket sẽ được lưu trữ trên máy chủ và có thể tải về từ thư mục uploads.

Giao Tiếp Thời Gian Thực: Tích hợp WebSocket để gửi và nhận tin nhắn và tệp tin một cách nhanh chóng và hiệu quả, trong thời gian thực.

- Kỹ Thuật & Công Nghệ Sử Dụng

Flask: Framework Python nhẹ nhàng để xây dựng ứng dụng web.

Flask-SocketIO: Dễ dàng tích hợp WebSocket vào Flask, hỗ trợ giao tiếp thời gian thực.

RSA và DES3: Các thuật toán mã hóa và chữ ký để bảo vệ dữ liệu, đảm bảo tính bảo mật khi truyền tải thông tin.

HTML, CSS, JavaScript: Được sử dụng để xây dựng giao diện người dùng tương tác và dễ sử dụng.

Socket TCP: Để giao tiếp giữa client và server khi gửi nhận tệp tin.

- Giao Diện Người Dùng

Giao diện người dùng được thiết kế đơn giản và dễ sử dụng, cung cấp các tính năng cơ bản như nhập tin nhắn, chọn tệp tin để gửi, và hiển thị các thông báo khi tệp tin hoặc tin nhắn được gửi hoặc nhận thành công. Giao diện được thiết kế tối giản, nhưng vẫn đảm bảo tính thẩm mỹ và dễ sử dụng.ư

![image](https://github.com/user-attachments/assets/275f9202-18ba-4634-b986-a395793a257c)

