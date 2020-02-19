import os

file_list_1 = os.listdir(r'E:\WDJ_Data\DATA\DATA\20200117\CT')
file_list_2 = os.listdir(r'E:\WDJ_Data\DATA\20200117\CT')

for file_name in file_list_1:
    if file_name in file_list_2:
        print(file_name)