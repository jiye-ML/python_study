import os
import pandas as pd


def get_fracture_dict(fracture_df):
	_fracture_dict = dict()
	
	# iter data to save
	for _row_idx, _row in fracture_df.iterrows():
		print('get_fracture_dict', _row_idx)
		
		_columns = [
			'image_path', 'image_path1',
			'x', 'y', 'z',
			'width', 'height', 'depth',
			'label', 'pred', 'prob'
		]
		
		_image_name = os.path.basename(_row['image_path'])
		
		_fracture_dict[_image_name] = _row[_columns]
	
	return _fracture_dict


def get_pipeline_result_dict(data_frame):
	""" get dict from dataFrame """
	_pipeline_result_dict = dict()
	
	# prob class
	for _row in data_frame.iterrows():
		_row = _row[1]
		_image_path = _row['image_path']
		_pipeline_result_dict[_image_path] = _row['class']
	
	return _pipeline_result_dict

	
if __name__ == '__main__':
	_csv_file_path = 'xxx'
	_data_frame = pd.read_csv(_csv_file_path, 'gbk')
	get_fracture_dict(_data_frame)
