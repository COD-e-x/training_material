import socket

HOST = '127.0.0.1'
PORT = 50000


def start_server(host, port):
    try:
        # server = socket.create_server((host, port))
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((host, port))  # назначив адрес, определяем socket сервером
            server.listen(1)  # слушатель порта (многопоточность)
            while True:
                print('Сервер работает...')
                client_socket, address = server.accept()  # принимает запрос, разделяет на клиента и адрес
                data = client_socket.recv(1024).decode('utf-8')  # получаем содержимое клиента
                print(f'Запрос:\n{data}')
                content = load_page(data)
                client_socket.send(content)
                client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        if server:
            server.close()
        print('Сервер выключен.')


def load_page(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nConnection: close\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\nConnection: close\r\n\r\n'

    # Полное содержание запроса (request_data)
    # ['GET', '/contact.html', 'HTTP/1.1', 'Host:', '127.0.0.1:50000', 'Connection:', 'keep-alive', 'sec-ch-ua:', '"Not',
    #  'A(Brand";v="8",', '"Chromium";v="132",', '"Microsoft', 'Edge";v="132"', 'sec-ch-ua-mobile:', '?0',
    #  'sec-ch-ua-platform:', '"Windows"', 'Upgrade-Insecure-Requests:', '1', 'User-Agent:', 'Mozilla/5.0', '(Windows',
    #  'NT', '10.0;', 'Win64;', 'x64)', 'AppleWebKit/537.36', '(KHTML,', 'like', 'Gecko)', 'Chrome/132.0.0.0',
    #  'Safari/537.36', 'Edg/132.0.0.0', 'Accept:',
    #  'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    #  'Sec-Fetch-Site:', 'same-origin', 'Sec-Fetch-Mode:', 'navigate', 'Sec-Fetch-User:', '?1', 'Sec-Fetch-Dest:',
    #  'document', 'Referer:', 'http://127.0.0.1:50000/home.html', 'Accept-Encoding:', 'gzip,', 'deflate,', 'br,', 'zstd',
    #  'Accept-Language:', 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7']

    path = request_data.split()[1]
    try:
        with open('views' + path, 'rb') as file:
            response = file.read()
        return HDRS.encode('utf-8') + response
    except FileNotFoundError:
        return (HDRS_404 + 'Извините! Такой страницы не существует.').encode('utf-8')


if __name__ == '__main__':
    start_server(HOST, PORT)
