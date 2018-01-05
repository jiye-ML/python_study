'''
    邮件
'''
from email.header import Header
from email import encoders
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEBase, MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class ToolEmail:

    def __init__(self, subject='主题', sender='database_homework@163.com',
                 password='123456', name='jiye',
                 smtp_server='smtp.163.com', receiver=[""]):
        self.__subject = subject
        self.__sender = sender
        self.__password = password
        self.__name = name
        self.__smtp_server = smtp_server
        self.__receiver = receiver

        # 新建邮件
        self.root = MIMEMultipart()
        self.root['from'] = self.format_address('%s <%s>' % (self.__name, self.__sender))
        self.root['To'] = self.__receiver[0]
        self.root['Subject'] = Header(self.__subject, 'utf-8')

        pass

    # 格式化邮件
    @staticmethod
    def format_address(string):
        name, address = parseaddr(string)
        return formataddr(Header(name, 'utf-8').encode(), address)

    # 添加文本
    def add_plain(self, value):
        mime_text = MIMEText(value, 'plain', 'utf-8')
        self.root.attach(mime_text)

    # 添加图片附件
    def add_attachment_img(self, name, path='', image_type='png'):
        self._add_attachment(self._get_path(name, path), "Data", image_type, name)

    # 添加文本附件
    def add_attachment_txt(self, name, path=""):
        self._add_attachment(self._get_path(name, path), 'text', 'txt', name)

    # 添加附件，需指定 maintype,subtype
    def add_attachment(self, name, maintype, subtype, path=""):
        self._add_attachment(self._get_path(name, path), maintype, subtype, name)

    def _add_attachment(self, file, maintype, subtype, name):
        with open(file, 'rb') as f:
            mime = MIMEBase(maintype, subtype, filename=name)
            mime.add_header("Content-Disposition", 'attachment', filename=name)
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            # 添加
            self.root.attach(mime)

    # 组装路径
    @staticmethod
    def _get_path(name, path):
        file_path = name
        if len(path) > 0:
            if path[-1] == '/':
                file_path = path + name
            else:
                file_path = path + '/' + name
        return file_path

    # 发送邮件
    # 在构造函数中初始化参数： ToolEmail(self, subject, sender, password, name, smtp_server, receiver)
    # 可在发送前设置主题: set_subject(value)
    # 添加邮件正文： add_plain(value)
    # 添加图片附件: add_attachment_img(name, path=None, image_type='png')
    # 添加文件附件： add_attachment_txt(name, path=None)
    # 发送： send_email()
    def send_email(self, level=0):
        # 发送
        try:
            smtp_obj = smtplib.SMTP(self.__smtp_server, 25)
            smtp_obj.set_debuglevel(level)
            smtp_obj.login(self.__sender, self.__password)
            smtp_obj.sendmail(self.__sender, self.__receiver, self.root.as_string())
            smtp_obj.quit()
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")

    pass


if __name__ == "__main__":
    base_path = "../data/ToolEmail/"
    my_email = ToolEmail(subject="主题名称")
    my_email.add_plain(value="This is first email")
    my_email.add_attachment_img(name=base_path + "demo_email.png")
    my_email.add_attachment_txt(name=base_path + "demo_email.txt")
    my_email.add_attachment(name=base_path + "demo_email.png", maintype="Data", subtype="png")
    my_email.send_email(level=0)