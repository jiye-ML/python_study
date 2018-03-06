'''
    和文件相关一些操作
'''

import pickle
from scipy.io import loadmat
from scipy.io import savemat


class CoreFile:

    # pkl 保存文件
    @staticmethod
    def write_to_pkl(path, data):
        with open(path, 'wb') as f:
            pickle.dump(data, f)
        pass

    # pkl 读取文件
    @staticmethod
    def read_from_pkl(path):
        with open(path, 'rb') as f:
            return pickle.load(f)
        pass

    # txt 写
    @staticmethod
    def write_to_txt(path, data):
        with open(path, 'w') as f:
            f.write(data)
        pass

    # txt 读
    @staticmethod
    def read_from_txt(path):
        with open(path, 'r') as f:
            return f.read()
        pass

    # mat 写
    @staticmethod
    def write_to_mat(path, dict_data):
        if not isinstance(dict_data, dict):
            raise TypeError
        savemat(path, dict_data)

    # mat 读
    @staticmethod
    def read_all_from_mat(path):
        return loadmat(path)

    @staticmethod
    def read_col_from_mat(path, col):
        return loadmat(path)[col]

    pass


if __name__ == '__main__':

    base_path = "../data/CoreFile/"
    pkl_path = base_path + "test.pkl"
    txt_path = base_path + "test.txt"
    mat_path = base_path + "test.mat"

    # pkl
    data = {"a": "aaa",
            "b": "bbb"}

    CoreFile.write_to_pkl(pkl_path, data)
    print(CoreFile.read_from_pkl(pkl_path))

    # txt
    data = "1234"
    CoreFile.write_to_txt(txt_path, data)
    print(CoreFile.read_from_txt(txt_path))

    # mat
    data_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    data_b = [[2, 2, 3], [5, 5, 6], [8, 8, 9]]
    data = {"data_a": data_a, "data_b": data_b}
    print(CoreFile.read_all_from_mat(mat_path))
    print(CoreFile.read_col_from_mat(mat_path, "data_a"))