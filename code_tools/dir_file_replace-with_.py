import os

file_dir = r'E:\jiye-study\AI\python_study'

current_path = os.getcwd()
os.chdir(r'E:\jiye-study\AI\python_study')

for _file in os.listdir(file_dir):
  os.rename(_file, _file.replace('Inheritance_', '12.'))

os.chdir(current_path)