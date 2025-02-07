from tkinter import *
import tkinter.ttk as ttk
import modifiedtk as mtk
import functions as f

def t1_confirm():
    text = t1_textbox.get("1.0", END)
    print(f.findNames(text))


root = Tk() 
root.title("Auto PPT")
root.geometry("960x720")



# Adding Tab
mainTab = ttk.Notebook(root)
tab1 = ttk.Frame(mainTab)
tab2 = ttk.Frame(mainTab)
mainTab.add(tab1, text ='파일 생성') 
mainTab.add(tab2, text ='Tab 2') 
mainTab.pack(expand = 1, fill ="both") 



##########Tab1##########
# t1_frame1 = Frame(tab1, width=300, height=370, background="#9E9E9E")
# t1_frame2 = Frame(tab1, width=660, height=370, background="#707070")
# t1_frame3 = Frame(tab1, width=960, height=250, background="#B5B5B5")
# t1_frame4 = Frame(tab1, width=960, height=80, background="red")

t1_frame1 = Frame(tab1, width=300, height=370)
t1_frame2 = Frame(tab1, width=660, height=370)
t1_frame3 = Frame(tab1, width=960, height=290)
t1_frame4 = Frame(tab1, width=960, height=60)

t1_frame1.place(x=0, y=0)
t1_frame2.place(x=300, y=0)
t1_frame3.place(x=0, y=370)
t1_frame4.place(x=0, y=660)
t1_frame1.pack_propagate(False)
t1_frame2.pack_propagate(False)
t1_frame3.pack_propagate(False)
t1_frame4.pack_propagate(False)


# Frame 1
# textbox
t1_textbox_frame = Frame(t1_frame1)
t1_textbox_frame.pack(fill="both", expand="True")
t1_textbox_frame2 = Frame(t1_frame1)
t1_textbox_frame2.pack(side="bottom", fill="x")
t1_btn_confirm = Button(t1_textbox_frame2, text="검색", width=10, command= t1_confirm)
t1_btn_confirm.pack(side="right", padx=5, pady=5)

t1_scrollbar = Scrollbar(t1_frame1)
t1_scrollbar.pack(side="right", fill="y")
t1_textbox = mtk.PlaceholderText(t1_frame1,
                                 placeholder="순서가 입력된 문자열을 입력하십시오\n형식(0 또는 0.)을 만족해야 합니다.",
                                 yscrollcommand=t1_scrollbar.set)
t1_textbox.pack(side="left", fill = "both", expand="True")
t1_scrollbar.config(command=t1_textbox.yview)







# Frame 2
# search frame
t1_search_frame = Frame(t1_frame2)
t1_search_frame.pack(fill="x")

t1_txt_search = mtk.PlaceholderEntry(t1_search_frame, "가수 이름, 찬양 제목으로 검색")
t1_txt_search.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

t1_btn_search = Button(t1_search_frame, text="검색", width=10)
t1_btn_search.pack(side="right", padx=5, pady=5)

# lists frame
t1_list_frame = Frame(t1_frame2)
t1_list_frame.pack(fill="y", expand=True)

t1_list = mtk.SortableTable(t1_list_frame)

t1_btn_append = Button(t1_list_frame, text="추가", width=10)
t1_btn_append.pack(side="right", padx=5, pady=5)

# Frame 3
# list
t1_list2 = Listbox(t1_frame3)
t1_list2.pack(fill=BOTH, expand= True)



# Frame 4
t1_btns_frame = Frame(t1_frame4)
t1_btns_frame.place(x=5, y=0)

t1_btn0 = Button(t1_btns_frame, text = "간주", width=5)
t1_btn0.pack(side="left", padx=5, pady=5)
t1_btn1 = Button(t1_btns_frame, text = "V1", width=5)
t1_btn1.pack(side="left", padx=5, pady=5)
t1_btn2 = Button(t1_btns_frame, text = "V2", width=5)
t1_btn2.pack(side="left", padx=5, pady=5)
t1_btn3 = Button(t1_btns_frame, text = "V3", width=5)
t1_btn3.pack(side="left", padx=5, pady=5)
t1_btn4 = Button(t1_btns_frame, text = "V4", width=5)
t1_btn4.pack(side="left", padx=5, pady=5)
t1_btn5 = Button(t1_btns_frame, text = "P-Ch", width=5)
t1_btn5.pack(side="left", padx=5, pady=5)
t1_btn6 = Button(t1_btns_frame, text = "Ch", width=5)
t1_btn6.pack(side="left", padx=5, pady=5)
t1_btn7 = Button(t1_btns_frame, text = "Bridge", width=5)
t1_btn7.pack(side="left", padx=5, pady=5)
t1_btn8 = Button(t1_btns_frame, text = "Undo", width=5)
t1_btn8.pack(side="left", padx=5, pady=5)
t1_btn9 = Button(t1_btns_frame, text = "Done", width=5)
t1_btn9.pack(side="left", padx=5, pady=5)

t1_btn_exit = Button(t1_frame4, text = "종료", width=10, command=exit)
t1_btn_exit.place(x=870,y=5)
t1_btn_save = Button(t1_frame4, text = "내보내기", width=10)
t1_btn_save.place(x=780,y=5)

presetval = ["Preset1", "Preset2","Preset3"]
t1_combobox = ttk.Combobox(t1_frame4, height=10, values=presetval, state="readonly")
t1_combobox.current(0)
t1_combobox.place(x=600,y=8)
t1_combobox.set("Set Preset")


# p_var = DoubleVar()
# progress_bar = ttk.Progressbar(t1_frame4, maximum=100, variable=p_var)
# progress_bar.place(x=5,y=45, width=945)

# Executing Program
root.resizable(False, False)
root.mainloop()

