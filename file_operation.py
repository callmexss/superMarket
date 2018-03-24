import os


def get_specific_file(filetype=""):
    return [x for x in os.listdir() if x.endswith(filetype)]


def get_specific_file_count(filetype=""):
    return len(get_specific_file(filetype))


def create_a_file(filename):
    with open(filename, "w") as f:
        f.write("")


def gen_specific_file(filetype, n):
    for i in range(1, n + 1):
        create_a_file(str(i)+"."+filetype)


def delete_specific_file(filetype):
    print("warning!!! This operation will delete all the {} files in current directory".format(filetype))
    choose = input("Are you sure you want to delete all the files? (y/n) ")
    if (choose.lower() == 'y'):
        [os.remove(file) for file in get_specific_file(filetype)]
    else:
        print("cancel...")

def delete_file_less_than(size, filetype="JPG"):
    files = get_specific_file(filetype)
    [os.remove(file) for file in files if os.path.getsize(file) <= size]
    


# test
def test():
    create_a_file("test.txt")
    gen_specific_file("txt", 10)
    count = get_specific_file_count("txt")
    print(count)
    delete_specific_file("txt")
    count = get_specific_file_count("txt")
    print(count)
