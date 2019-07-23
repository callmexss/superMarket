import os
import shutil
import random
from send2trash import send2trash


def get_specific_file(filetype="JPG"):
    return [x for x in os.listdir() if x.endswith(filetype.lower()) or x.endswith(filetype.upper())]


def get_specific_file_count(filetype="JPG"):
    return len(get_specific_file(filetype.lower()))


def create_a_test_file(filename):
    with open(filename, "w") as f:
        f.write("")


def gen_specific_test_file(filetype, n):
    for i in range(1, n + 1):
        create_a_test_file(str(i)+"."+filetype)


def delete_specific_file(filetype):
    assert(filetype.lower() != 'py')
    print("warning!!! This operation will delete all the {} files in current directory.".format(filetype))
    choose = input("Are you sure you want to delete all the files? (y/n) ")
    if (choose.lower() == 'y'):
        [send2trash(file) for file in get_specific_file(filetype)]
    else:
        print("cancel...")


def delete_file_less_than(size, filetype="JPG"):
    size = size * 1024
    files = get_specific_file(filetype)
    for file in files:
        if os.path.getsize(file) < size:
            send2trash(file)
    # [send2trash(file) for file in files if os.path.getsize(file) / 1024 < size]


def delete_file_larger_than(size, filetype="JPG"):
    files = get_specific_file(filetype)
    for file in files:
        if os.path.getsize(file) / 1024 > size:
            send2trash(file)
    # [send2trash(file) for file in files if os.path.getsize(file) / 1024 > size]


def count_file_in_size(size, filetype="JPG"):
    files = get_specific_file(filetype)
    file_in_size = [f for f in files if abs(
        os.path.getsize(f) / 1024 - size) < 1]
    print("{}: {}".format(str(size), len(file_in_size)))
    return len(file_in_size)


def get_file_size(filename):
    return os.path.getsize(filename)


def get_file_size_ordered():
    files = get_specific_file("JPG")
    li = [os.path.getsize(file)//1024 for file in files]
    return list(set(li))


def random_move():
    files = get_specific_file()
    if not os.path.isdir("replace"):
        os.mkdir("replace")

    target_file = files[random.randint(0, len(files) - 1)]
    shutil.move(target_file, os.path.join("replace", target_file)) 


def random_move_until2(target_num):
    try:
        os.mkdir("replace")
    except:
        print("folder already exists.")
    while get_specific_file_count() != target_num:
        # print("start random delete...")
        random_move()
    print("random move till {} finished...".format(target_num))

# test


def test():
    # create_a_test_file("test.txt")
    gen_specific_test_file("txt", 100)
    count = get_specific_file_count("txt")
    print(count)
    delete_specific_file("txt")
    count = get_specific_file_count("txt")
    print(count)


# test()
