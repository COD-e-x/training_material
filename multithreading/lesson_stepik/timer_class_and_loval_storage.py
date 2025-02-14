import time
import threading

# ===== Timer ==========================================================================================================


# def my_test():
#     while True:
#         print('test')
#         time.sleep(1)
#
#
# threading.Timer(10, my_test).start()
#
# while True:
#     print('111')
#     time.sleep(2)

# ======================================================================================================================

# def my_test():
#     while True:
#         print('test')
#         time.sleep(1)
#
#
# thr = threading.Timer(5, my_test)
# thr.start()
#
# for _ in range(3):
#     print('111')
#     time.sleep(1)
#
# thr.cancel()
# print('finish')

# ======================================================================================================================

# import time
# import threading
#
# def my_test():
#     while True:
#         print('test')
#         time.sleep(1)
#
#
# thr = threading.Timer(2, my_test)
# thr.setDaemon(True)
# thr.start()
#
# for _ in range(6):
#     print('111')
#     time.sleep(1)
#
# print('finish')

# ===== Local storage ==================================================================================================

# data = threading.local()
#
# def get_name():
#     print(data.name)
#
# def t1():
#     data.name = threading.currentThread().name
#     get_name()
#
# def t2():
#     data.name = threading.currentThread().name
#     get_name()
#
#
# threading.Thread(target=t1, name='t1').start()
# threading.Thread(target=t2, name='t2').start()

# ======================================================================================================================

data = threading.local()


def get_name():
    # if hasattr(data, 'name'):
    #     print(data.name)
    # else:
    #     print('name не установлено для этого потока')
    print(data.name)


def t1():
    data.name = threading.currentThread().name
    # time.sleep(5)
    get_name()


threading.Thread(target=t1, name='t1').start()
# time.sleep(1)
# get_name()
