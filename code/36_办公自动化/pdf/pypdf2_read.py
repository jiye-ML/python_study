# 使用pypdf2读取pdf文件内容
# 读出来的内容（有问题) 主要是没空格
import PyPDF2

filename = 'The Youtube video recommendation system.pdf'
pdfFileObj=open(filename, 'rb')
pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj=pdfReader.getPage(0)
print(pageObj.extractText())

