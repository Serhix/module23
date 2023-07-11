import logging
from multiprocessing import cpu_count, Pool, current_process
import multiprocessing
from timeit import default_timer



logger = logging.getLogger()
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('logs_procces.txt', mode='a', encoding=None, delay=False, errors=None)
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


def factorize_one_procces(number):
    num_list = []
    for num in range(1, number+1):
        if number % num == 0:
            num_list.append(num)
    return num_list


@execution_time
def factorize(*number):
    max_worker = cpu_count() * 2 + 1
    # max_worker = 1
    with Pool(processes=max_worker) as pool:
        result = pool.map(factorize_one_procces, number)
    logger.debug(f'{max_worker} processes worked')
    return result
    raise NotImplementedError() # Remove after implementation


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')  
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
