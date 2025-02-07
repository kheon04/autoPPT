from tkinter import *
import tkinter.ttk as ttk
import modifiedtk as mtk
import functions as f

root = Tk() 
root.title("Auto PPT")
root.geometry("960x720")



# Adding Tab
mainTab = ttk.Notebook(root)
tab1 = ttk.Frame(mainTab)
tab2 = ttk.Frame(mainTab)
mainTab.add(tab1, text ='파일 생성') 
mainTab.add(tab2, text ='DB 추가') 
mainTab.pack(expand = 1, fill ="both") 



##########Tab1##########
t2frame2_width=400
t2_frame1 = Frame(tab1, width=t2frame2_width, height=695)
t2_frame2 = Frame(tab1, width=560, height=695, background="#707070")
# t1_frame1 = Frame(tab1, width=300, height=370)
# t1_frame2 = Frame(tab1, width=660, height=370)

t2_frame1.place(x=0, y=0)
t2_frame2.place(x=400, y=0)
t2_frame1.pack_propagate(False)
t2_frame2.pack_propagate(False)

t2_list_frame1 = LabelFrame(t2_frame1, text="파일 불러오기")
t2_list_frame1.place(x=0,y=0)

t2_list_frame2 = Frame(t2_list_frame1)
t2_list_frame2.pack(side="bottom")

t2_list_scroll = Scrollbar(t2_list_frame2)
t2_list_scroll.pack(side="right", fill="y")

t2_listbox = Listbox(t2_list_frame2, selectmode="extended", height=33, yscrollcommand=t2_list_scroll.set, width=52)
t2_listbox.pack(side="left", fill="both", expand="True")
t2_list_scroll.config(command=t2_listbox.yview)




#option frame
option_frame = LabelFrame(t2_frame1, text="Option",width=t2frame2_width-10)
option_frame.place(x=0,y=560)

#1. 가사 위치 옵션
lbl_insslide = Label(option_frame, text="가사 위치", width=10)
lbl_insslide.pack(padx=7, pady=7, side="left")

option_insslide = ["제목", "부제목", "부부제목"]
cmb_insslide = ttk.Combobox(option_frame, state="readonly", values=option_insslide, width=10)
cmb_insslide.current(1)
cmb_insslide.pack(padx=7, pady=7, side="left")

#2. 섹션 분리 옵션
lbl_insslide = Label(option_frame, text="섹션 여부", width=10)
lbl_insslide.pack(padx=7, pady=7, side="left")

option_insslide = ["무시", "포함"]
cmb_insslide = ttk.Combobox(option_frame, state="readonly", values=option_insslide, width=10)
cmb_insslide.current(0)
cmb_insslide.pack(padx=7, pady=7, side="left")

t2_btn_find = Button(t2_frame1, text="파일 열기", width=10)
t2_btn_find.place(x=220,y=620)
t2_btn_start = Button(t2_frame1, text="시작", width=10)
t2_btn_start.place(x=310,y=620)

# Frame2
t2_userTyping_frame = LabelFrame(t2_frame2, text="직접 입력")
t2_userTyping_frame.pack(fill=BOTH, expand=TRUE)





# Executing Program
# root.resizable(False, False)
root.mainloop()

