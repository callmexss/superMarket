from __future__ import print_function

import os
import sys
from lxml import etree

is_py3 = sys.version_info[0] == 3

files = [x for x in os.listdir(os.getcwd()) if x.endswith('xml')]

first = -2
second = -1
which = 0

if is_py3:
    goods_type = input("How many goods? 1 or 2: ")
else:
    goods_type = raw_input("How many goods? 1 or 2: ")

if goods_type == '2':
    if is_py3:
        seq = input("which one do you want to change? 1 or 2: ")
    else:
        seq = raw_input("which one do you want to change? 1 or 2: ")

    if seq == '1':
        which = first
    elif seq == '2':
        which = second
    else:
        raise Exception("Wrong label!")
elif goods_type == '1':
    which = second



if is_py3:
    change2 = input("which label do you want to change to: ")
else:
    change2 = raw_input("which label do you want to change to: ")

for file in files:
    doc = etree.parse(file)
    root = doc.getroot()
    children = root.getchildren()
    # print(children)
    obj = children[which]
    # print(obj.tag)
    if obj.tag != 'object':
        raise Exception("Wrong xml file!")
    if is_py3:
        obj.getchildren()[0].text = change2
    else:
        obj.getchildren()[0].text = bytes(change2)
    doc.write(file)
    print("change label for {}".format(file))
    # label_from_file = []
    # for child in children:
    #   if child.tag == "object":
    #     label_from_file.append(child)
    # if len(label_from_file) == 2:
    #   print("change label for {}".format(file))
    #   label_from_file[which].getchildren()[0].text = change2
    #   doc.write(file)

if is_py3:
    input()
else:
    raw_input()