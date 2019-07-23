import os
from lxml import etree

files = [x for x in os.listdir() if x.endswith('xml')]

first = -2
second = -1
which = 0

seq = input("which one do you want to change? 1 or 2: ")

if seq == '1':
  which = first
elif seq == '2':
  which = second
else:
  raise Exception("Wrong label!")

change2 = input("which label do you want to change to: ")

for file in files:
  doc = etree.parse(file)
  root = doc.getroot()
  children = root.getchildren()
  obj = children[which]
  if obj.tag != 'object':
    raise Exception("Wrong xml file!")
  obj.getchildren()[0].text = change2
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