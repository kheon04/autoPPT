import os
from tkinter import *
import tkinter.messagebox as msgbox



root_name = "windows 메모장"
root = Tk()
root.title(root_name)
root.geometry("960x720")




#text를 받을 지점과 스크롤바설정
 
frame1 = Frame(root, relief="solid")
frame1.pack(side="left", fill = "both", expand="True")

scrollbar = Scrollbar(frame1)
scrollbar.pack(side="right", fill="y")

textbox = Text(frame1, yscrollcommand=scrollbar.set)
textbox.pack(side="left", fill = "both", expand="True")

scrollbar.config(command=textbox.yview)



#열기, 저장 파일 이름
filepath = "mynote.txt"


def openfile():
    if os.path.isfile(filepath):
        global openqui
        openqui = IntVar()
        openqui = msgbox.askokcancel(root_name, "메모장에서의 내용은 덮어씌워집니다.\n진행하시겠습니까?")
        if openqui ==1:
            with open(filepath,'r', encoding="UTF-8") as f:
                textbox.delete("1.0", END)
                textbox.insert(END, f.read())
                print("openfile_cmd")
        else:
            pass
    else:
        msgbox.showerror(root_name, "설정된 경로에서 파일을 찾을 수 없습니다.")
    


def savefile():
    global savequi
    savequi = IntVar()
    savequi = msgbox.askokcancel(root_name, "이전파일의 내용은 덮어씌워집니다.\n진행하시겠습니까?")
    if savequi ==1:
        with open(filepath, 'w', encoding="UTF-8") as f:
            f.write(textbox.get("1.0",END))
            print("savefile_cmd")
    else:
        pass


#menu
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=openfile)
menu_file.add_command(label="저장", command=savefile)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command= root.quit)
menu.add_cascade(label="파일(F)", menu=menu_file)

menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집(E)", menu=menu_edit)
menu_format = Menu(menu, tearoff=0)
menu.add_cascade(label="서식(O)", menu=menu_format)
menu_view = Menu(menu, tearoff=0)
menu.add_cascade(label="보기(V)", menu=menu_view)
def menu_help():
    print("help_cmd")
menu.add_command(label="도움말", command=menu_help)



root.config(menu=menu)
root.mainloop()