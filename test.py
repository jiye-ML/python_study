import pandas as pd


_importance_title = ['单据号', '供应商', '物料编码', '数量']

_caigou = r'D:\2020年1月采购收货确认终稿.xls'
_wuliao = r'D:\3月份之前单据.xlsx'

_caigou_data_frame = pd.read_excel(_caigou)
_wuliao_data_frame = pd.read_excel(_wuliao)

_caigou_groups = _caigou_data_frame.groupby(by=_importance_title)
_wuliao_groups = _wuliao_data_frame.groupby(by=_importance_title)

_number_not_match = []
_caigou_but_no_wuliao = []
_wuliao_but_no_caigou = []
for _key1, _group1 in _caigou_groups:

  _group2 = None

  # 采购有， 物料没有
  try:
    _group2 = _wuliao_groups.get_group(_key1)
  except KeyError as e:
    _caigou_but_no_wuliao.append(_key1)
    continue

  _caigou_count = len(_group1)
  _wuliao_count = len(_group2)

  if _caigou_count < _wuliao_count:
    _wuliao_but_no_caigou.append(_key1)
  elif _wuliao_count < _caigou_count:
    _caigou_but_no_wuliao.append(_key1)

for _key2, _group2 in _wuliao_groups:
  try:
    _group1 = _caigou_groups.get_group(_key2)
  except KeyError as e:
    _wuliao_but_no_caigou.append(_key2)

_caigou_but_no_wuliao_data_frame = pd.DataFrame(_caigou_but_no_wuliao)
_caigou_but_no_wuliao_data_frame.to_csv(r'D:\_caigou_but_no_wuliao.csv', encoding='gbk')

_wuliao_but_no_caigou_data_frame = pd.DataFrame(_wuliao_but_no_caigou)
_wuliao_but_no_caigou_data_frame.to_csv(r'D:\_wuliao_but_no_caigou.csv', encoding='gbk')



