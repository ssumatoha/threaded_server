import socket

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()

print('Соединение с сервером')
sock.connect((HOST, PORT))  # Указываем, что хост локальный и порт 9090
message = str(input('Введите сообщение: '))
print('Отправка данных серверу')
sock.send(message.encode())  # Отправляем с клиента на сервер hello (Серв принимает только байт-код)

print('Приём данных от сервера')
data = sock.recv(1024)
sock.close()

print(data.decode())
print('Разрыв соединения с сервером')
