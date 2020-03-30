import os
import pandas as pd
import numpy as np


one_data_frame = pd.read_csv(

)
another_data_frame = pd.read_csv(

)

one_file_list = list(set(one_data_frame['image_path'].tolist()))
another_file_list = another_data_frame['filename'].tolist()

diff = np.intersect1d(one_file_list, another_file_list)
print(diff)

