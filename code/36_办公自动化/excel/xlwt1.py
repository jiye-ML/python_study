# 写入 楼宇安防.xls
import xlwt

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('国贸写字楼')

# 写入excel，参数对应 行, 列, 值
worksheet.write(0, 0, label='人员')
# 保存文件
workbook.save('./楼宇安防2.xls')

""" 设置字体样式 """
# 初始化样式
style = xlwt.XFStyle()
# 为样式创建字体
font = xlwt.Font()
font.name = 'Times New Roman'
# 加粗
font.bold = True
# 下划线
font.underline = True
# 斜体字
font.italic = True
# 设定样式
style.font = font
worksheet.write(0, 1, '体温', style)  # 带样式的写入
workbook.save('楼宇安防2.xls')

""" 设置单元格宽度 """
# worksheet = workbook.add_sheet('世贸天阶')
worksheet.write(0, 2, '时间')
# 设置单元格宽度
worksheet.col(0).width = 3333
workbook.save('./楼宇安防2.xls')

""" 添加日期到单元格 """
import datetime

# 获取样式
style = xlwt.XFStyle()
# Oth er options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
style.num_format_str = 'M/D/YY'
worksheet.write(1, 2, datetime.datetime.now(), style)
workbook.save('楼宇安防2.xls')

""" 向单元格添加一个公式 """
worksheet.write(1, 1, 37.4)
worksheet.write(2, 1, 36.5)
# 求两个单元格的平均值
worksheet.write(3, 1, xlwt.Formula('AVERAGE(B2,B3)'))
workbook.save('楼宇安防2.xls')

""" 向单元格添加一个链接 """
worksheet.write(1, 3, xlwt.Formula('HYPERLINK("http://www.baidu.com";"baidu")'))
workbook.save('楼宇安防2.xls')

""" 合并列和行 """
# write_merge(行开始, 行结束，列开始, 列结束, '数据内容')
# 创建字体
font = xlwt.Font()
# 加粗
font.bold = True
style = xlwt.XFStyle()
style.font = font
worksheet.write_merge(4, 5, 0, 2, '备注：需要检查是否佩戴口罩', style)
workbook.save('楼宇安防2.xls')

""" 给单元格添加边框和背景色 """
# 边框样式
borders = xlwt.Borders()
borders.left = xlwt.Borders.DASHED
borders.right = xlwt.Borders.DASHED
borders.top = xlwt.Borders.DASHED
borders.bottom = xlwt.Borders.DASHED
borders.left_colour = 0x40
borders.right_colour = 0x40
borders.top_colour = 0x40
borders.bottom_colour = 0x40
# 创建样式
style = xlwt.XFStyle()
style.borders = borders
worksheet.write(1, 0, '张飞', style)
worksheet.write(2, 0, '关羽', style)
workbook.save('楼宇安防2.xls')
