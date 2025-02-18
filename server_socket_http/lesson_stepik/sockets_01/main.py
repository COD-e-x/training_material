import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 2000))
server.listen()
print('Сервер запущен...')

while True:
    client_socket, address = server.accept()
    request = client_socket.recv(1024).decode('utf-8')

    print(f'Запрос:\n{request}')

    if '/request' in request:
        HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nConnection: close\r\n\r\n'
        body = '<html><body><h1>Запрос успешно обработан!</h1></body></html>'
        response = HDRS + body
        client_socket.send(response.encode('utf-8'))
    elif '/close' in request:
        HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nConnection: close\r\n\r\n'
        body = '<html><body><h1>Сервер выключается...</h1></body></html>'
        response = HDRS + body
        client_socket.send(response.encode('utf-8'))
        client_socket.close()
        print('Соединение закрыто...')
        print('Сервер выключен.')
        break # выключаем сервер

    else:
        HDRS = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=utf-8\r\nConnection: close\r\n\r\n'
        body = '<html><body><h1>404 - неизвестный запрос.</h1></body></html>'
        response = HDRS + body
        client_socket.send(response.encode('utf-8'))
        print('404 - неизвестный запрос.')

    client_socket.close()
