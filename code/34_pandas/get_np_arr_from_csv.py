import pandas as pd


def get_np_arr_from_csv(csv, columns=None, encoding='gbk'):

  if columns is None:
    raise Exception('columns is none')

  _df = pd.read_csv(csv, encoding=encoding)
  _np_arr = _df[columns].to_numpy()
  _np_arr = _np_arr.squeeze()

  return _np_arr
