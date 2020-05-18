# 拆分PDF
from PyPDF2 import PdfFileReader, PdfFileWriter

def split(filename, name_of_split):
    pdf = PdfFileReader(filename)
    # 拆分，即读取PDF中的每页，单独进行保存
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

filename = 'course.pdf'
split(filename, 'course_page')