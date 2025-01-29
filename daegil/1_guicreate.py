from tkinter import *
import tkinter.ttk as ttk



"""프로그래밍 순서
0. gui의 형태를 먼저 스케치해야함
1. root와 frame, 기초적인 버튼등을 배치 (레이아웃)
2. 기본적인 함수를 정의 (버튼 등이 동작하도록)
3. 기능적인 함수를 정의(기능을 요구하는 함수) 3.1, 3.2 등의 저장을 요구

"""


root = Tk()
root.title("auto PPT")


#dir frame
dir_frame = LabelFrame(root, text="directory select")
dir_frame.pack(fill="x", padx=5, pady=5)

txt_dir_path = Entry(dir_frame)
txt_dir_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_lst_reload = Button(dir_frame, text="새로고침", width=10)
btn_lst_reload.pack(side="right", padx=5, pady=5)

btn_dir_path = Button(dir_frame, text="찾아보기", width=10)
btn_dir_path.pack(side="right", padx=5, pady=5)


#combineframe1
combineframe1 = Frame(root)
combineframe1.pack(fill="x", padx=5, pady=5)

#list frame
lst_frame1 = LabelFrame(combineframe1, text="ppt list")
lst_frame1.pack(side="left", padx=5, pady=5)

lst_frame2 = Frame(lst_frame1)
lst_frame2.pack(padx=5, pady=5)

lst_scroll = Scrollbar(lst_frame2)
lst_scroll.pack(side="right", fill="y")

lst_ppt = Listbox(lst_frame2, selectmode="extended", height=25, yscrollcommand=lst_scroll.set, width=38)
lst_ppt.pack(side="left", fill="both", expand="True")
lst_scroll.config(command=lst_ppt.yview)

btn_lst_select = Button(lst_frame1, text="선택적용", width=10)
btn_lst_select.pack(side="right", padx=5, pady=5)


#selected ppt frame
slc_frame = LabelFrame(combineframe1, text="selected ppt")
slc_frame.pack(side="right", padx=5, pady=5, fill="y")

slc_list = Listbox(slc_frame, height=5, selectmode="extended", width=38)
slc_list.pack(fill="both", expand="True", padx=5, pady=5)

btn_slc_del = Button(slc_frame, text="선택삭제", width=10)
btn_slc_del.pack(side="right", padx=5, pady=5)


#option frame
option_frame = LabelFrame(root, text="option")
option_frame.pack(padx=5, pady=5, fill="x")

#1. 중간 슬라이드 개수 옵션
lbl_insslide = Label(option_frame, text="삽입슬라이드", width=10)
lbl_insslide.pack(padx=7, pady=7, side="left")

option_insslide = ["1개", "2개", "3개"]
cmb_insslide = ttk.Combobox(option_frame, state="readonly", values=option_insslide, width=10)
cmb_insslide.current(0)
cmb_insslide.pack(padx=7, pady=7, side="left")

#2. 우상단 워터마크 옵션
lbl_marking = Label(option_frame, text="워터마크", width=10)
lbl_marking.pack(side="left", padx=7, pady=7)

option_useornot = ["사용", "제거"]
cmb_marking = ttk.Combobox(option_frame, state="readonly", values=option_useornot, width=10)
cmb_marking.current(0)
cmb_marking.pack(side="left", padx=7, pady=7)

#3. 애니메이션 옵션
lbl_animation = Label(option_frame, text="에니매이션", width=10)
lbl_animation.pack(side="left", padx=7, pady=7)

cmb_animation = ttk.Combobox(option_frame, state="readonly", values=option_useornot, width=10)
cmb_animation.current(1)
cmb_animation.pack(side="left", padx=7, pady=7)


#progressbar frame
frame_progress = LabelFrame(root, text="progress")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)


#run frame
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5, ipady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command = root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12)
btn_start.pack(side="right", padx=5, pady=5)











root.resizable(False, False)
root.mainloop( )