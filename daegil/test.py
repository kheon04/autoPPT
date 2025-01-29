#윈도우 파일명 읽기
import os
from tkinter import filedialog


# cwd = os.getcwd()
# print(cwd)
# print("\.\pptlist")
# lst_ppt = os.listdir(".\daegil\lst_ppt")
# print(lst_ppt)
# curdir = os.curdir()
# print(curdir)

# a = "1.pptx"
# print(a[-5:])


file = filedialog.askopenfilename(title="파일을 선택하세요", 
        filetypes=(("powerpoint 파일", "*.pptx"), ("모든 파일", "*.*")),
        initialdir= "C:/Users/bluec/Documents/카카오톡 받은 파일")
print(file)
name = file[::-1]
print(name.find("/"))
a = name.find("/")
print(file[-name.find("/"):-5])