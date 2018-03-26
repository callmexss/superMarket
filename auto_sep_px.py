import file_operation
import os


pic_files = file_operation.get_specific_file("JPG")
xml_files = file_operation.get_specific_file("xml")

pic_dir = "pic"
xml_dir = "xml"

try:
  os.mkdir(pic_dir)
  os.mkdir(xml_dir)
except:
  print("folders already exist.")

for pic in pic_files:
  os.rename(pic, os.path.join(pic_dir, pic))

for xml in xml_files:
  os.rename(xml, os.path.join(xml_dir, xml))