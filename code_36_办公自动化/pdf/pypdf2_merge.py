# 导入读写pdf模块
from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()
    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
             # 将每页添加到writer对象
             pdf_writer.addPage(pdf_reader.getPage(page))
    # 写入合并的pdf
    with open(output, 'wb') as out:
    	pdf_writer.write(out)

paths = ['course.pdf', '2018高新认证名单.pdf']
merge_pdfs(paths, output='merged.pdf')
