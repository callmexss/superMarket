from __future__ import print_function

import os
import re
import time
import shutil
import threading

from pprint import pprint


def _test():
    """For Doctest
    """

    import doctest
    doctest.testmod()


def get_all_folders():
    """Get all folders in current path
    
    Returns:
        list -- folders in a list
    """

    return [x for x in os.listdir(os.getcwd()) if os.path.isdir(x)]


def get_info(folder):
    '''Get information from folder name

    Arguments:
        folder {string } -- Folder name 

    Returns:
        list -- Information from folder name

    >>> get_info('21-1')
    ['21', '1']
    >>> get_info('19-23-3')
    ['19', '23', '3']
    '''

    p = re.compile(r'\d+')
    return re.findall(p, folder)


def process(folder):
    """Main process of folder formation
    
    Arguments:
        folder {string} -- A folder to be formated
    """

    if folder == 'pic' or folder == 'xml':
        return

    path_list = []

    for root, _, files in os.walk(folder):
        if files:
            path_list.extend(os.path.join(root, x) for x in files)

    for file in path_list:
        if os.path.exists(file):
            if file.endswith('xml'):
                # print('move {} to xml ...'.format(file))
                shutil.move(file, 'xml')
            elif file.endswith('jpg') or file.endswith('JPG'):
                # print('move {} to pic ...'.format(file))
                shutil.move(file, 'pic')


def run(li):
    """For thread use
    
    Arguments:
        li {list} -- Parts of given root folders
    """

    for each in li:
        process(each)


def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Total time {} seconds".format((end - start)))

    return wrapper


@calculate_time
def test_speed():
    """Test speed
    """

    tag = input('multi or single? m or s: ')

    try:
        os.mkdir('pic')
        os.mkdir('xml')
    except Exception as e:
        print('Try to create folders failed, reason is ', e)

    folders = get_all_folders()
    if tag == 'm':
        length = len(folders)
        step = length // 5
        thread_list = []

        for i in range(0, length, step):
            if i + step <= length:
                thread_list.append(
                    threading.Thread(target=run, args=(folders[i:i + step], )))
            else:
                thread_list.append(
                    threading.Thread(target=run, args=(folders[i:], )))

        [t.start() for t in thread_list]
        [t.join() for t in thread_list]
    elif tag == 's':
        for folder in folders:
            process(folder)

    print("finished.")


def main():
    """Main function
    """

    try:
        os.mkdir('pic')
        os.mkdir('xml')
    except Exception as e:
        print('Try to create folders failed, reason is ', e)

    folders = get_all_folders()
    length = len(folders)
    step = length // 5 # threads number
    thread_list = []

    for i in range(0, length, step):
        if i + step <= length:
            thread_list.append(
                threading.Thread(target=run, args=(folders[i:i + step], )))
        else:
            thread_list.append(
                threading.Thread(target=run, args=(folders[i:], )))

    [t.start() for t in thread_list]
    [t.join() for t in thread_list]

    print("Auto move finished.")
    print("checking ...")
    pic_without_ext = set([x.split('.')[0] for x in os.listdir('pic')])
    xml_without_ext = set([x.split('.')[0] for x in os.listdir('xml')])
    print('Total get {} pictures and {} xml files'.format(
        len(pic_without_ext), len(xml_without_ext)))

    res = pic_without_ext - xml_without_ext
    if res:
        raise Exception("TOTAL FILES COUNT WRONG.")

    print('Finshed')


if __name__ == '__main__':
    main()