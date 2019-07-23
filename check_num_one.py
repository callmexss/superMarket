import os
import re
import time

total = 54

def process():
    li = [x for x in os.listdir()]
    count = 0

    if len(li) != total:
        count = total - len(li)
        print("Still have {} to draw".format(count))
        return False

    return True


def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Total time {} hours".format((end - start) / 3600))

    return wrapper

    
@calculate_time  
def main_loop():
    while not process():
        time.sleep(60)


if __name__ == '__main__':
    main_loop()