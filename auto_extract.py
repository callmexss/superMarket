import os
import shutil
import time
# import pickle

from pprint import pprint

# os.chdir(r'D:\Supermarket\1212\palyground\goutu2')
# os.listdir()

if not os.path.exists('../workdir'):
    os.mkdir('../workdir')

work_path = os.path.abspath('../workdir')
# print(work_path)


def get_full_path():
    full_path_list = []
    for root, _, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('jpg'):
                path = os.path.join(root, file)
                abs_path = os.path.abspath(path)
                full_path_list.append(abs_path)
    return full_path_list
    


def generate_hash_table(full_path_list):
    hash_table = {}
    for path in full_path_list:
        base_path, base_name = os.path.split(path)
        xml_path = base_path.replace('pic', 'xml')
        uid = base_name.split('.')[0]
        hash_table[uid] = xml_path

        # pickle.dump(hash_table, f)
        # pprint(hash_table)
    return hash_table


def classify_by_type():
    folder_list = list(set([x[:-2] for x in os.listdir() if os.path.isdir(x)]))
    # print(folder_list)
    final_list = []
    for folder in folder_list:
        path = os.path.join(work_path, folder)
        final_list.append((path, folder))
        if not os.path.isdir(path):
            os.mkdir(path)
    return final_list


def copy2workdir(full_path_list, final_list):
    for path in full_path_list:
        for each in final_list:
            if each[1] in path:
                base_name = os.path.split(path)[1]
                try:
                    shutil.copy(path, os.path.join(each[0], base_name))
                except Exception as err:
                    # print('cp {} -> {}'.format(path, os.path.join(each[0], base_name)))
                    print(err)
    print('auto move done!')


def get_all_xml_path(final_list):
    folder_path = [x[0] for x in final_list]
    # print(folder_path)
    xml_path = []
    for folder in folder_path:
        for root, _, files in os.walk(folder):
            for file in files:
                if file.endswith('xml'):
                    xml_path.append(os.path.abspath(os.path.join(root, file)))

    return xml_path


def send_them_back(xml_path, hash_table):
    for xml in xml_path:
        base_name = os.path.split(xml)[1]
        uid = base_name.split('.')[0]
        target = hash_table[uid]
        src = xml
        dst = os.path.join(target, base_name)
        try:
            shutil.copy(src, dst)
        except Exception as err:
            print('cp {} -> {}'.format(src, dst))
            print(err)

    print('send them back done!')




if __name__ == '__main__':
    choice = input('What do you want? (1. auto move to work dir; 2. send them back!): ')
    final_list = classify_by_type()
    full_path_list = get_full_path()
    hash_table = generate_hash_table(full_path_list)
    if choice == '1':
        copy2workdir(full_path_list, final_list)

    elif choice == '2':
        # for send them back
        xml_path = get_all_xml_path(final_list)
        send_them_back(xml_path, hash_table)

    time.sleep(3)
        