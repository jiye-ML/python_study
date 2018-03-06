from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()

# 窗口大小及位置
width = 300
height = 300
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry("%dx%d+%d+%d" % (width, height, (sw - width)//2, (sh - 2 * height)//2))


# 显示图片
label = Label(root)
label.grid(columnspan=2, row=0, ipadx=50, ipady=20)


def show_img():
    filename = "data/study_pil/alisure.jpg"
    im = Image.open(filename)
    im = im.resize((200, 200))
    global photo
    photo = ImageTk.PhotoImage(im)
    label["Data"] = photo
    return photo
    pass

show_img()


# 相应按钮点击事件
def click_button_1():
    messagebox.showinfo("info", "im info")


def click_button_2():
    print("click_button_1")

# 按钮
# http://blog.csdn.net/aa1049372051/article/details/51859476
btn = Button(root, text="0", command=click_button_1, width=10, height=1,
             bg="#678", bd=0, relief="groove")
btn.grid(column=0, row=1, padx=10, pady=10, sticky="e")
btn2 = Button(root, text="1", command=click_button_2, width=10, height=1,
              bg="#876", bd=0, relief="groove")
btn2.grid(column=1, row=1, padx=10, pady=10, sticky="w")

# 启动主循环
root.mainloop()
