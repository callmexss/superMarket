import os
import threading
import time

import file_operation
'''some data
11 208/669 11/669
12 327/588 0/588
13 371/665 0/665
14 144/661 33/661 
'''

TARGET_NUMBER = 100
TOTAL_NUMBER = file_operation.get_specific_file_count()
MAX_RATE = 0.618

os.system("show_folder_info.py")


def random_move():
    if file_operation.get_specific_file_count() > TARGET_NUMBER:
        file_operation.random_move_until2(TARGET_NUMBER)


def auto_decrease():
    # total_size = 0
    size_range = file_operation.get_file_size_ordered()
    low_quality = int(len(size_range) * MAX_RATE)
    # print(size_range[low_quality])
    # for size in size_range[low_quality:]:
    # total_size += file_operation.count_file_in_size(size)
    high_quality = int(len(size_range) * 0.90)
    # print(size_range[high_quality])
    print("delete files less than {}".format(size_range[low_quality]))
    delete_low_quality = threading.Thread(
        target=file_operation.delete_file_less_than,
        args=(size_range[low_quality], ))
    delete_low_quality.start()
    delete_low_quality.join()
    # file_operation.delete_file_less_than(size_range[low_quality])
    print("delete files larger than {}".format(size_range[high_quality]))
    # file_operation.delete_file_larger_than(size_range[high_quality])
    delete_high_quality = threading.Thread(
        target=file_operation.delete_file_larger_than,
        args=(size_range[high_quality], ))
    delete_high_quality.start()
    delete_high_quality.join()
    print("current file count: {}, finished...".format(
        file_operation.get_specific_file_count()))


if __name__ == '__main__':
    auto_decrease()
    random_move()

# while len(current("JPG")) != TARGET_NUMBER:
# auto_decrease()
