import file_operation

l_kb = 1024
l_mb = l_kb * 1024 # 未使用

target_size = input("想要删除小于多少(kb)的文件？ ")

# 当前默认是jpg类型，后面有需要再改
before = file_operation.get_specific_file_count("JPG")
print("当前共有{}个目标文件，开始删除...".format(before))

file_operation.delete_file_less_than(eval(target_size) * l_kb)

after = file_operation.get_specific_file_count("JPG")
print("小于{}kb的文件已被删除，还剩余{}个文件".format(target_size, after))