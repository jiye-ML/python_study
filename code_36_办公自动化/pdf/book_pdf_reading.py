# 提取指定PDF中的文本，图片
import urllib
import importlib,sys
importlib.reload(sys)
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams, LTTextBox, LTFigure, LTImage, LTCurve, LTChar
from pdfminer.pdfpage import PDFTextExtractionNotAllowed, PDFPage
from pdfminer.utils import get_bound, apply_matrix_pt
import os
from binascii import b2a_hex


# 图片保存路径
images_folder = './images'
# 保存图片
def save_image(lt_image, page_num):
    """Try to save the image data from this LTImage object, and return the file name, if successful"""
    result = None
    if lt_image.stream:
        file_stream = lt_image.stream.get_rawdata()
        if file_stream:
            file_ext = determine_image_type(file_stream[0:4])
            if file_ext:
                #file_name = ''.join([str(image_index), '_', lt_image.name, file_ext])
                file_name = ''.join([str(page_num), '_', lt_image.name, file_ext])
                if write_file(images_folder, file_name, file_stream, flags='wb'):
                    result = file_name
    return result

# 写文件
def write_file (folder, filename, filedata, flags='w'):
    """Write the file data to the folder and filename combination
    (flags: 'w' for write text, 'wb' for write binary, use 'a' instead of 'w' for append)"""
    result = False
    if os.path.isdir(folder):
        try:
            file_obj = open(os.path.join(folder, filename), flags)
            file_obj.write(filedata)
            file_obj.close()
            result = True
        except IOError:
            pass
    return result

def determine_image_type (stream_first_4_bytes):
    """Find out the image file type based on the magic number comparison of the first 4 (or 2) bytes"""
    file_type = None
    #bytes_as_hex = b2a_hex(stream_first_4_bytes)
    bytes_as_hex = b2a_hex(stream_first_4_bytes).decode(encoding='utf-8')
    if bytes_as_hex.startswith('ffd8'):
        file_type = '.jpeg'
    elif bytes_as_hex == '89504e47':
        file_type = '.png'
    elif bytes_as_hex == '47494638':
        file_type = '.gif'
    elif bytes_as_hex.startswith('424d'):
        file_type = '.bmp'
    return file_type

# 解析LTFigure
def parse_lt_figure(x, page_num, f=None):
    # LTFigure有children
    for lt_obj in x:
        print(lt_obj)
        if isinstance(lt_obj, LTImage):
            saved_file = save_image(lt_obj, page_num)
            print('save image ' + lt_obj.name)
        if isinstance(lt_obj, LTFigure):
            parse_lt_figure(lt_obj, page_num, f)
        if isinstance(lt_obj, LTChar): 
            print(lt_obj.get_text())
            f.write(lt_obj.get_text())


def parse(DataIO, save_path, start=None, end=None):
    # 用文件对象创建一个PDF文档分析器
    parser = PDFParser(DataIO)
    # 创建一个PDF文档
    doc = PDFDocument(parser)
    #分析器和文档相互连接
    parser.set_document(doc)
    #doc.set_parser(parser)
    # 提供初始化密码，没有默认为空
    #doc.initialize()
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
        #pages = PDFPage.get_pages(doc)
        # doc.get_pages()获取page列表
        #for page in pages:
        page_num = 0
        for page in PDFPage.create_pages(doc):
            page_num = page_num + 1
            if start is not None and end is not None:
                if page_num < start:
                    continue
                if page_num > end:
                    break
            interpreter.process_page(page)
            # 接收该页面的LTPage对象
            layout = device.get_result()
            f = open('./text/'+str(page_num)+'.txt', 'w')
            #with open('%s' % (save_path), 'a') as f:

            # 这里的layout是一个LTPage对象 里面存放着page解析出来的各种对象
            # 一般包括LTTextBox，LTFigure，LTImage，LTTextBoxHorizontal等等一些对象
            # 想要获取文本就得获取对象的text属性
            for x in layout:
                #try:
                if isinstance(x, LTTextBoxHorizontal):
                    # 得到文本
                    result = x.get_text()
                    try:
                        print("***************** LTTextBoxHorizontal  ************")
                        print(result)
                        #if len(result) >= 15:
                        # 写到文件中
                        f.write(result + "\n")
                    except:
                        print('写入文件错误', result)
                        pass
                if isinstance(x, LTTextBox): 
                    print("***************** LTTextBox  ************")
                    print(x.get_text())
                if isinstance(x, LTFigure): 
                    print("***************** LTFigure  ************")
                    parse_lt_figure(x, page_num, f)
                if isinstance(x, LTImage): 
                    print("***************** LTImage  ************")
                    saved_file = save_image(x, page_num)
                    print('save image ' + x.name)
                if isinstance(x, LTChar): 
                    print('ppppppppppppppp')
                    print(x.get_text())
                    f.write(x.get_text())
                if isinstance(x, LTCurve): 
                    print("***************** LTCurve  ************")
            f.close()

# 解析本地PDF文本，保存到本地TXT
#filename = 'Deep Neural Networks for YouTube Recommendations-2016.pdf'
#filename = 'The Youtube video recommendation system.pdf'
filename = 'book.pdf'
with open(filename,'rb') as pdf_html:
    parse(pdf_html, r'./result.txt', 1, 50)
