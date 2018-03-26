import os
import file_operation


root_path = os.path.split(__file__)[0]
program_path = "labelImg.exe"
final_path = os.path.join(root_path, program_path)

for file in file_operation.get_specific_file("JPG"):
  # print(final_path + " " + file)
  os.system(final_path + " " + file)