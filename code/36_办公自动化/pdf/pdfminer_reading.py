# 提取指定论文中的文本，图片
import urllib
import importlib,sys
importlib.reload(sys)
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams, LTTextBox, LTFigure, LTImage, LTCurve
from pdfminer.pdfpage import PDFTextExtractionNotAllowed, PDFPage
 
 
def parse(DataIO, save_path):
    # 用文件对象创建一个PDF文档分析器
    parser = PDFParser(DataIO)
    # 创建一个PDF文档
    doc = PDFDocument(parser)
    #分析器和文档相互连接
    parser.set_document(doc)
    # 检查文档是否可以转成TXT，如果不可以就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDF资源管理器，来管理共享资源
        rsrcmagr = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        # 将资源管理器和设备对象聚合
        device = PDFPageAggregator(rsrcmagr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmagr, device)
 
        # 循环遍历列表，每次处理一个page内容
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
            # 接收该页面的LTPage对象
            layout = device.get_result()
            # 这里的layout是一个LTPage对象 里面存放着page解析出来的各种对象
            # 一般包括LTTextBox，LTFigure，LTImage，LTTextBoxHorizontal等等一些对象
            # 想要获取文本就得获取对象的text属性
            for x in layout:
                try:
                    if(isinstance(x, LTTextBoxHorizontal)):
                        with open('%s' % (save_path), 'a') as f:
                            #print("***************** LTTextBoxHorizontal  ************")
                            # 得到文本
                            result = x.get_text()
                            #print (result)
                            # 写到文件中
                            f.write(result + "\n")
                except:
                    if(isinstance(x, LTTextBox)): 
                        print("***************** LTTextBox  ************")
                        #print(x.get_text())
                    if(isinstance(x, LTFigure)): 
                        print("***************** LTFigure  ************")
                        #print(x.get_text())
                    if(isinstance(x, LTImage)): 
                        print("***************** LTImage  ************")
                        #print(x.get_text())
                    if(isinstance(x, LTCurve)): 
                        print("***************** LTCurve  ************")
                        
                    #print("Failed")
            break
    f.close()
 
 
# 解析本地PDF文本，保存到本地TXT
filename = 'The Youtube video recommendation system.pdf'
with open(filename,'rb') as pdf_html:
    parse(pdf_html, r'./result.txt')
