import os
from lxml import etree
from pprint import pprint


dirs = [x for x in os.listdir() if os.path.isdir(x)]

def get_label(dir_name):
  '''Get two goods' label from a directory name
  
  Arguments:
    dir_name {[string]} -- Directory name
  
  Returns:
    [list] -- Two goods' label in a list

  >>> get_label('2-7-3')
  ['2', '7']
  '''

  return dir_name.split('-')[:2]


def _test():
  import doctest
  doctest.testmod()


def get_xml_dirs():
  xml_folder = []
  for root, _, __ in os.walk(os.getcwd()):
    # find xml folder
    if root.endswith('xml'):
      xml_folder.append(root)
  return xml_folder


def check_number(path):
  files = os.listdir(path)
  if len(files) != 216:
    print("Error!!! The file number of {} is wrong.".format(path))


def process(each, file):
  tree = etree.parse(os.path.join(each, file))
  label_list = get_label(each.split('\\')[-1])
  # print(label_list)
  root = tree.getroot()
  children = root.getchildren()
  label_from_file = []
  for child in children:
    if child.tag == "object":
      label = child.getchildren()[0].text
      label_from_file.append(label)
      # if label not in label_list:
        # print(f"Error! Wrong label: {label} in {os.path.join(each, file)}")
  if len(label_from_file) != 2:
    print("Error! Wrong label account: {0} in {1}".format(len(label_from_file), os.path.join(each, file)))
	# print(f"Error! Wrong label account: {len(label_from_file)} in {os.path.join(each, file)}")
    print("It should be {}".format(len(label_list)))
	# print(f"It should be {len(label_list)}")

  if set(label_from_file) != set(label_list):
    # print(f"Error! Wrong label: {set(label_from_file)} in {os.path.join(each, file)}")
	  print("Error! Wrong label: {0} in {1}".format(set(label_from_file), os.path.join(each, file)))
    # print(f"It should be {set(label_list)}")
	  print("It should be {}".format(set(label_list)))


def check_label(each):
  xml_files = os.listdir(each)
  for file in xml_files:
    process(each, file)


if __name__ == '__main__':
    _test()
    xml_folder = get_xml_dirs()
    pprint(xml_folder)

    for each in xml_folder:
      check_number(each)
      check_label(each)
      
    input("Press any key to exit.")