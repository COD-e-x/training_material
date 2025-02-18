import socket
import logging

HOST = '127.0.0.1'
PORT = 65432

logging.basicConfig(level=logging.INFO)

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print('Клиент подключился к серверу...')
        while True:
            try:
                user_input = input('Введите текст для передачи на сервер: ')
                if not user_input:
                    print('\nВы не ввели данные.')
                else:
                    if user_input == 'Отключиться':
                        client.sendall(user_input.encode())
                        logging.info('Клиент закрыл соединение.')
                        break
                    else:
                        client.sendall(user_input.encode())
                        response = client.recv(1024).decode()
                        print(f'Полученные данные {response}.')
            except KeyboardInterrupt:
                print(f'\nСоединение с сервером было закрыто принудительно.')
                break
            except ConnectionError as e:
                print('Программа на вашем хост-компьютере разорвала установленное подключение.')
                break
            except Exception as e:
                print(f'Неизвестная ошибка: {e}')
                break
except ConnectionRefusedError:
    print('Сервер недоступен.')
