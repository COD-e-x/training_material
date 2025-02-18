from threading import Thread
import socket
import logging


HOST = '127.0.0.1'
PORT = 65432

logging.basicConfig(level=logging.INFO)


def handle_connection(sock, addr):
    with sock:
        while True:
            try:
                data = sock.recv(1024)
                if not data:
                    logging.info(f'Данные не поступили от клиента {addr}. '
                                 f'\n\t\t  Возможно, некорректное отключение. '
                                 f'\n\t\t  Сервер разорвал соединение с клиентом {addr}!')
                    break
                data = data.decode()
                if data == 'Отключиться':
                    logging.info(f'Клиент {addr} закрыл соединение, связь разорвана.')
                    sock.close()
                    break
                else:
                    logging.info(f'Приняты данные ({data}) от: {addr}.')
                    response = data.upper()
                    sock.sendall(response.encode())
                    logging.info(f'Отправлены данные ({response}): {addr}.')
            except ConnectionError as e:
                logging.error(f'Ошибка соединения с клиентом {addr}: {e}.')
                break
            except Exception as e:
                logging.error(f'Неизвестная ошибка: {e}')
                break


if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(1)
        print('Сервер запушен...')
        logging.info('Ожидание подключения.')
        while True:
            connect, address = server.accept()
            thr = Thread(target=handle_connection, args=(connect, address))
            logging.info(thr)
            logging.info(f'Подключен клиент {address}.')
            thr.start()
