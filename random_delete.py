import os
import random


target_number = input("输入要保留的照片数量：")
target_type = input("请输入图片扩展名：")

while(len([x for x in os.listdir() if x.endswith(target_type)]) > eval(target_number)):
    pictures = [x for x in os.listdir() if x.endswith(target_type)]
    os.remove(pictures[random.randint(0, len(pictures) - 1)])

print("当前目录下共有{}张图片".format(len(pictures) - 1))
