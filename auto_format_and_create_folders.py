from __future__ import print_function
import os
import re
import shutil
from pprint import pprint


def _test():
    import doctest
    doctest.testmod()


def get_info(folder):
    
    p = re.compile(r'\d+')
    return re.findall(p, folder)


def get_folders():
    """Get all folders
    
    Returns:
        list -- All folders
    """

    return [x for x in os.listdir(os.getcwd()) if os.path.isdir(x)]


def rename_folders():
    folders = get_folders()

    for folder in folders:
        new_name = '-'.join(get_info(folder))
        os.rename(folder, new_name)


def auto_create(folder):
    """Auto create folders
    
    Arguments:
        folder {string} -- folder name
    """

    os.chdir(folder)
    base_name = os.getcwd().split('\\')[-1]
    # print(base_name)
    names = ['top', 'down']

    xml_folder = base_name + '-xml'
    pic_folder = base_name + '-pic'

    try:
        os.mkdir(xml_folder)
        os.mkdir(pic_folder)
    except:
        pass

    for each in names:
        if os.path.isdir(each):
            shutil.move(each, pic_folder)

    xml_path = os.path.join(os.getcwd(), xml_folder)
    try:
        os.mkdir(os.path.join(xml_path, 'top-xml'))
        os.mkdir(os.path.join(xml_path, 'down-xml'))
    except:
        pass

    os.chdir("..")


if __name__ == '__main__':
    rename_folders()
    folders = get_folders()
    pprint(folders)
    for folder in folders:
        print("create folder for {} successfully".format(folder))
        auto_create(folder)

    input("Press any key to exit.")