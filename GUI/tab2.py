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



##########Tab2##########
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


# TODO
"""
기능 추가
옵션의 버튼과 글자간 간격 줄이기
rel형태로 제작하도록 하기
직접 입력 부분에 어떤 것을 추가할지 생각
"""

#option frame
option_frame = LabelFrame(t2_frame1, text="Option")
option_frame.place(relheight=.12, relwidth=1.0, relx=0.0,rely=0.8)
option_frame1 = Frame(option_frame, background="black")
option_frame1.place(relheight=0.5, relwidth=1.0,relx=0.0,rely=0.0)
option_frame2 = Frame(option_frame)
option_frame2.place(relheight=0.5, relwidth=1.0,relx=0.0,rely=0.5)

#1. 가사 위치 옵션
lbl_insslide = Label(option_frame1, text="가사 위치")
lbl_insslide.place(relwidth=0.3333,relheight=1.0, relx=0.0, rely=0.0)

option_insslide = ["제목", "부제목", "부부제목"]
cmb_insslide = ttk.Combobox(option_frame2, state="readonly", values=option_insslide, width=12)
cmb_insslide.current(1)
cmb_insslide.place(relwidth=0.3,relheight=.7, relx=0.015, rely=.15)

#2. 섹션 분리 옵션
lbl_insslide = Label(option_frame1, text="섹션 여부")
lbl_insslide.place(relwidth=0.3333,relheight=1.0, relx=0.3333, rely=0.0)

option_insslide = ["무시", "포함"]
cmb_insslide = ttk.Combobox(option_frame2, state="readonly", values=option_insslide, width=12)
cmb_insslide.current(0)
cmb_insslide.place(relwidth=0.3,relheight=.7, relx=0.3333+.015, rely=.15)

#2. 섹션 분리 옵션
lbl_insslide = Label(option_frame1, text="제목 설정", width=12)
lbl_insslide.place(relwidth=0.3333,relheight=1.0, relx=0.6666, rely=0.0)

option_insslide = ["직접 설정", "파일 이름"]
cmb_insslide = ttk.Combobox(option_frame2, state="readonly", values=option_insslide, width=12)
cmb_insslide.current(1)
cmb_insslide.place(relwidth=0.3,relheight=.7, relx=0.6666+.015, rely=.15)

t2_btn_frame1 = Frame(t2_frame1)
t2_btn_frame1.place(x=0,y=660,relwidth=1.0)
t2_btn_start = Button(t2_btn_frame1, text="시작", width=10)
t2_btn_start.pack(side="right",padx=5,pady=5)
t2_btn_find = Button(t2_btn_frame1, text="파일 열기", width=10)
t2_btn_find.pack(side="right",padx=5,pady=5)

# Frame2
t2_userTyping_frame = LabelFrame(t2_frame2, text="직접 입력")
t2_userTyping_frame.pack(fill=BOTH, expand=TRUE)





# Executing Program
# root.resizable(False, False)
root.mainloop()

