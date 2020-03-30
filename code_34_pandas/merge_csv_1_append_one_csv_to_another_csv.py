import pandas as pd


_csv_path = '{}'.format(
)
_another_csv_path = '{}'.format(
)
_result_csv_path = '{}'.format(
)
_data_frame = pd.read_csv(_csv_path)
_another_data_frame = pd.read_csv(_another_csv_path)

_columns = _data_frame.columns
_result_data_frame = _data_frame.append(_another_data_frame)
_result_data_frame.to_csv(_result_csv_path, columns=_columns, index=False)
