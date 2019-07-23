import os
import re
import time

total = 108

def get_label(dir_name):
    '''Get goods' label from a directory name

    Arguments:
        dir_name {string} -- Directory name
    
    Returns:
        list -- Two goods' label in a list

    >>> get_label('2-7-3')
    ['2', '7']
    >>> get_label('9-2')
    ['9']
    >>> get_label('10-11-2-xml')
    ['10', '11']
    '''

    p = re.compile(r'\d+')
    return re.findall(p, dir_name)[:-1]


def process():
    li = [x for x in os.listdir()]
    count = 0

    if len(li) != total:
        count = total - len(li)
        print("Still have {} to draw".format(count))
        return False
    else:
        from lxml import etree
        for file in li:
            doc = etree.parse(file)
            root = doc.getroot()
            children = root.getchildren()
            if len(children) != 8:
                count += 1
        
        if count == 0:
            print("Finished!")
            return True
        else:
            print("Still have {} to draw".format(count))
            return False


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