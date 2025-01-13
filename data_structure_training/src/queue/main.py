from queue_class import Queue
from queue_menu_class import QueueMenu

def main():
    queue = Queue()
    queue_menu = QueueMenu(queue)
    queue_menu.display_menu()

    while True:
        try:
            user_choice = int(input('\nВыберите вариант предложенный в меню: '))
            queue_menu.process_choice(user_choice)
        except ValueError:
            print('\nОшибка: Выберите вариант предложенный в меню')
            continue


if __name__ == '__main__':
    main()