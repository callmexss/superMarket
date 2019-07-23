import file_operation


pic_files = file_operation.get_specific_file("jpg")
xml_files = file_operation.get_specific_file("xml")


pic_li = [x.split('.')[0] for x in pic_files]
xml_li = [x.split('.')[0] for x in xml_files]

print(set(pic_li) - set(xml_li))