import pandas as pd


def save_arr_to_csv(data, columns, output_path, encoding='gbk'):
  df = pd.DataFrame(data=data, columns=columns)
  df.to_csv(output_path, encoding=encoding, index=False)
