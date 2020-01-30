import os

file_dir = r'E:\jiye-study\AI\python_study'

current_path = os.getcwd()
os.chdir(r'E:\jiye-study\AI\python_study')

for _file in os.listdir(file_dir):

  if not (_file[3].isnumeric() and _file[4].isnumeric() and _file[5].isnumeric()):
    continue

  _new_file_name = '{}0{}_{}'.format(_file[0: 3], _file[3], _file[4:])

  os.rename(_file, _new_file_name.replace('-', '_'))

os.chdir(current_path)