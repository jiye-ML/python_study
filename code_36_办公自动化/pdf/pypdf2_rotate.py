import PyPDF2

# 对PDF文档进行旋转
def PDFrotate(origFileName,newFileName,rotation):
    pdfFile = open(origFileName,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    pdfWriter = PyPDF2.PdfFileWriter()
    # 对每一页进行旋转
    for page in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(page)
        pageObj.rotateClockwise(rotation)
        pdfWriter.addPage(pageObj)
    # 保存文件
    newFile = open(newFileName,'wb')
    pdfWriter.write(newFile)
    pdfFile.close()
    newFile.close()

PDFrotate('course.pdf', 'course_rotate.pdf', 270)

