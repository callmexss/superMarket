import os
import random

import file_operation


target_number = input("输入要保留的照片数量：")
target_type = input("请输入图片扩展名：")

while(file_operation.get_specific_file_count(target_type.lower()) > eval(target_number)):
    pictures = file_operation.get_specific_file(target_type)
    os.remove(pictures[random.randint(0, len(pictures) - 1)])

print("当前目录下共有{}张图片".format(len(pictures) - 1))
