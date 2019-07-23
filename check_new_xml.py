from __future__ import print_function

import os
import re
from lxml import etree
from pprint import pprint

dirs = [x for x in os.listdir(os.getcwd()) if os.path.isdir(x)]


def _test():
    import doctest
    doctest.testmod()


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


def check_number(pic_folder, xml_folder, goods_type):
    '''Check file numbers
    
    Arguments:
        pic_folder {string} -- Picture folder
        xml_folder {string} -- XML folder
        goods_type {integer} -- One good or two goods
    '''

    if goods_type == 1:
        number_should_be = 54
    elif goods_type == 2:
        number_should_be = 108
    else:
        raise Exception("Wrong goods type!")

    pic_files_without_ext = [
        os.path.splitext(x)[0] for x in os.listdir(pic_folder)
    ]
    xml_files_without_ext = [
        os.path.splitext(x)[0] for x in os.listdir(xml_folder)
    ]

    if len(set(pic_files_without_ext) ^ set(xml_files_without_ext)
           ) == number_should_be * 2:
        print('top and down folders may save reversed.')
        input('Check it and re-run again.')
        exit()

    if len(set(pic_files_without_ext) - set(xml_files_without_ext)) != 0:
        print("Something wrong, check {} and {}".format(pic_folder, xml_folder))

    if len(pic_files_without_ext) != number_should_be:
        print("Wrong number for {}".format(pic_folder))
    if len(xml_files_without_ext) != number_should_be:
        print("Wrong number for {}".format(xml_folder))
        print("The missing files are:")
        pprint([
            x + '.xml'
            for x in set(pic_files_without_ext) - set(xml_files_without_ext)
        ])


def check_label(xml_folder, label_should_be):
    '''Check label for xml folder
    
    Arguments:
        xml_folder {string} -- XML folder
        label_should_be {list} -- Label should be
    '''

    xml_files = [x for x in os.listdir(xml_folder) if x.endswith('xml')]
    for xml_file in xml_files:
        file_path = os.path.join(xml_folder, xml_file)
        tree = etree.parse(file_path)
        root = tree.getroot()
        children = root.getchildren()
        label_from_xml_file = []

        for child in children:
            if child.tag == 'object':
                label_from_xml_file.append(child.getchildren()[0].text)
        
        if len(label_from_xml_file) < len(label_should_be):
            print('Missing label for {}'.format(file_path))
        elif len(label_from_xml_file) > len(label_should_be):
            print('Multi label for {}'.format(file_path))
        elif set(label_from_xml_file) != set(label_should_be):
            print('Wrong label for {}'.format(file_path))



def check(folder):
    '''Check each folder
    
    Arguments:
        folder {string} -- Folder name
    '''

    if len(os.listdir(folder)) != 2:
        print("{} has something wrong, check it.".format(folder))
        return

    label_should_be = get_label(folder)
    goods_type = len(label_should_be)  # 1 for one good else 2

    path_list = []

    for root, dirnames, _ in os.walk(folder):
        path_list.extend([str(os.path.join(root, x)) for x in dirnames])

    # print(path_list)
    for path in path_list:
        if 'top' in path:
            if 'xml' in path:
                top_xml = path
            else:
                top_pic = path
        elif 'down' in path:
            if 'xml' in path:
                down_xml = path
            else:
                down_pic = path

    # print(top_pic)
    # print(top_xml)
    # print(down_pic)
    # print(down_xml)

    print('Checking for {} ...'.format(folder))
    check_number(top_pic, top_xml, goods_type)
    check_number(down_pic, down_xml, goods_type)

    check_label(top_xml, label_should_be)
    check_label(down_xml, label_should_be)
    print('-' * 50)


if __name__ == '__main__':
    for each in dirs:
        check(each)

    input('press any key to exit.')
