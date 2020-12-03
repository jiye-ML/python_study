# 读取楼宇安防.xls
import xlrd

data = xlrd.open_workbook('./楼宇安防.xls')

""" 
	获取工作簿（book）中的工作表（sheet）
	以下三个函数都会返回一个xlrd.sheet.Sheet()对象 
"""
# 通过索引顺序获取
table = data.sheets()[0]
# 通过索引顺序获取
table = data.sheet_by_index(0)
# 通过名称获取
table = data.sheet_by_name('Sheet1')

# 返回book中所有工作表的名字
names = data.sheet_names()
print(names)

""" 工作表中行/列的操作 """
# 获取该sheet中的有效行数
nrows = table.nrows
print(nrows)
row_index, col_index = 0, 0
# 获取某行信息
print(table.row(row_index))
print(table.row_slice(row_index))

# 获取某列信息
print(table.col(col_index))
print(table.col_slice(col_index))

# 返回某行的 数据类型列表
print(table.row_types(row_index, start_colx=0, end_colx=None))
print(table.row_types(1, start_colx=0, end_colx=None))

# 返回某行的数值
print(table.row_values(row_index, start_colx=0, end_colx=None))
# 返回某行的有效单元格长度
print(table.row_len(row_index))

""" 单元格操作 """
# 返回单元格对象
print(table.cell(row_index, col_index))
# 返回单元格中的数据类型
print(table.cell_type(row_index, col_index))
# 返回单元格中的数据
print(table.cell_value(row_index, col_index))
