from __future__ import print_function

import os
import re


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


def _rename(origin, new):
    """Rename original name to new name
    
    Arguments:
        origin {string} -- Original name
        new {string} -- New name
    """

    if origin == new:
        return
    try:
        os.rename(origin, new)
        print("Rename {} to {} successfully".format(origin, new))
    except Exception as err:
        print("Reanme {} failed.".format(origin))
        print("err: ", err)


def get_type(path):
    """Get file type in given folders.
    WARNING: Path must be like 3-1\\3-1-pic or 3-1\\3-1-xml
    
    Arguments:
        path {string} -- Folder path
    
    Returns:
        string -- Filetype
    """

    # print(path)
    all_files = []
    for _, __, files in os.walk(path):
        all_files.extend(files)

    # >>> os.path.splitext('xxx.jpg')
    # ('xxx', '.jpg')
    file_types = set([os.path.splitext(x)[1][1:] for x in all_files])
    if len(file_types) != 1:
        print("filetypes wrong in {}!".format(path))
        print(file_types)
    return file_types.pop()



def clean_root_level():
    """Rename folders in top level
    """

    folders = get_all_folders()
    for folder in folders:
        new_name = '-'.join(get_info(folder))
        _rename(folder, new_name)


def rename_xml_path(xml_path):
    """Rename xml folder
    
    Arguments:
        xml_path {string} -- XML folder path
    """

    if set(os.listdir(xml_path)) != {'top-xml', 'down-xml'}:
        xml_folders = []
        for root, dirnames, _ in os.walk(xml_path):
            xml_folders.extend([str(os.path.join(root, x)) for x in dirnames])

        for folder in xml_folders:
            if 'top' in folder:
                xml_base = os.path.split(folder)[0]
                # print(folder)
                # print(os.path.join(xml_base, 'top-xml'))
                _rename(folder, os.path.join(xml_base, 'top-xml'))
            elif 'down' in folder:
                xml_base = os.path.split(folder)[0]
                # print(folder)
                _rename(folder, os.path.join(xml_base, 'down-xml'))


def rename_pic_path(pic_path):
    """Rename picture folder
    
    Arguments:
        pic_path {string} -- Picture folder path
    """

    if not set(os.listdir(pic_path)) == {'top-pic', 'down-pic'}:
        # print(pic_path)
        pic_folders = []
        for root, dirnames, _ in os.walk(pic_path):
            pic_folders.extend([str(os.path.join(root, x)) for x in dirnames])

        for folder in pic_folders:
            if 'top' in folder:
                # print(folder)
                pic_base = os.path.split(folder)[0]
                # print(pic_base)
                _rename(folder, os.path.join(pic_base, 'top-pic'))
            elif 'down' in folder:
                # print(folder)
                pic_base = os.path.split(folder)[0]
                # print(pic_base)
                _rename(folder, os.path.join(pic_base, 'down-pic'))


def process(folder):
    """Main process of folder formation
    
    Arguments:
        folder {string} -- A folder to be formated
    """

    path_list = []

    for root, dirnames, _ in os.walk(folder):
        path_list.extend([str(os.path.join(root, x)) for x in dirnames])

    # print(path_list)
    for path in path_list:
        if not 'top' in path and not 'down' in path:
            if 'xml' in path:
                base, xml = path.split('\\')
                new_name = '-'.join(get_info(xml)) + '-xml'
                xml_path = os.path.join(base, new_name)
                _rename(path, xml_path)
                rename_xml_path(xml_path)
            elif 'pic' in path:
                base, pic = path.split('\\')
                new_name = '-'.join(get_info(pic)) + '-pic'
                pic_path = os.path.join(base, new_name)
                _rename(path, pic_path)
                rename_pic_path(pic_path)
            else:
                ext_name = get_type(path)
                if ext_name.lower() == 'jpg':
                    pic_base, pic_folder = os.path.split(path)
                    new_name = '-'.join(get_info(pic_folder)) + '-pic'
                    pic_path = os.path.join(pic_base, new_name)
                    _rename(path, pic_path)
                    rename_pic_path(os.path.join(pic_base, new_name))
                elif ext_name.lower() == 'xml':
                    xml_base, xml_folder = os.path.split(path)
                    new_name = '-'.join(get_info(xml_folder)) + '-xml'
                    xml_path = os.path.join(xml_base, new_name)
                    _rename(path, xml_path)
                    rename_xml_path(xml_path)
                else:
                    print("Something wrong in {}".format(folder))


if __name__ == '__main__':
    clean_root_level()
    folders = get_all_folders()
    for folder in folders:
        process(folder)