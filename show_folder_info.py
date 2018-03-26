import file_operation

count = file_operation.get_specific_file_count("JPG")
size_set = file_operation.get_file_size_ordered()

print("当前文件夹共有{}个文件".format(count))
print("其大小顺序为{}".format(size_set))