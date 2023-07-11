import logging
from timeit import default_timer


logger = logging.getLogger()
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs_func.txt', mode='a', encoding=None, delay=False, errors=None)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def execution_time(func):
    def delta_time(*args):
        t1 = default_timer()
        try:
            return func(*args)
        finally:
            delta = default_timer() - t1
            logging.info(f'Execution time: {delta}')
    return delta_time


@execution_time
def factorize(*number):
    result = []
    num_list = []
    for num in number:
        for n in range(1, num+1):
            if num % n == 0:
                num_list.append(n)
        result.append(num_list)
        num_list = []
    return result
    raise NotImplementedError() # Remove after implementation


a, b, c, d  = factorize(128, 255, 99999, 10651060)
assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
