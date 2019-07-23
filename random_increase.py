import os

import file_operation

target_num = 100
folder = "replace"

if file_operation.get_specific_file_count() < target_num:
  if os.path.isdir(folder):
    os.chdir(folder)
    print(os.getcwd())
    os.chdir("..")
    print(os.getcwd())