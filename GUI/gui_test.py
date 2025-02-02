from tkinter import *
from tkinter import filedialog
import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk


"""프로그래밍 순서
0. gui의 형태를 먼저 스케치해야함
1. root와 frame, 기초적인 버튼등을 배치 (레이아웃)
2. 기본적인 함수를 정의 (버튼 등이 동작하도록)
3. 기능적인 함수를 정의(기능을 요구하는 함수) 3.1, 3.2 등의 저장을 요구

"""
# sys.stdout = open('log.txt', 'a')


RootName = "AutoSlide"
root = Tk()
root.title(RootName)

def lst_reload():
    pass

def dir_pathfind():
    pass

def lst_reload():
    pass

def lst_reload():
    pass

def lst_reload():
    pass

def lst_reload():
    pass

def lst_reload():
    pass

def lst_reload():
    pass

# DB 저장, 불러오기



#combineframe1
combineframe1 = Frame(root)
combineframe1.pack(fill="x", padx=5, pady=5)


class SortableTable:
    def __init__(self, root):
        # self.root = root
        # self.root.title("Sortable Table Example")

        # Treeview 설정
        # columns = [(이름, width), ]
        self.columns = [("SongID", 50), ("아티스트", 80), ("이름", 200), ("수정한 날짜", 150)]
        column_names = [col[0] for col in self.columns]
        self.tree = ttk.Treeview(root, columns=column_names, show='headings')

        # 각 컬럼 헤더와 넓이, 정렬 설정
        for col in self.columns:
            self.tree.heading(col[0], text=col[0], command=lambda c=col[0]: self.sort_column(c, False))
            self.tree.column(col[0], width=col[1], anchor=tk.CENTER)

        # 데이터 삽입
        self.data = [
            (1, "NULL", "Born Again", "2025-01-29 17:26:13", "2025-01-29 17:26:13"),
            (2, "1001", "Dreams Alive", "2023-11-21 10:15:12", "2023-11-20 09:00:00"),
            (3, "1002", "Skyward", "2024-02-03 12:05:30", "2024-02-03 11:45:15")
        ]

        # 초기 데이터 삽입
        self.populate_table(self.data)

        # packing
        self.tree.pack(fill=tk.BOTH, expand=True)

    def populate_table(self, data):
        # 기존 데이터 삭제
        for row in self.tree.get_children():
            self.tree.delete(row)

        # 정렬된 데이터 삽입
        for row in data:
            self.tree.insert("", tk.END, values=row)

    def sort_column(self, col, reverse):
        # 현재 Treeview 데이터 가져오기
        data_list = [(self.tree.set(child, col), child) for child in self.tree.get_children("")]\
        # 데이터 정렬 (문자열/숫자 처리)
        # 자체적으로, column의 1, 2 번째 행은 float변환을 하지 않도록 예외처리
        data_list.sort(key=lambda t: (float(t[0]) if t[0].replace(".", "").isdigit() and (col != self.columns[1][0] and col != self.columns[2][0]) else t[0]), reverse=reverse)

        # 정렬된 데이터를 Treeview에 다시 삽입
        for index, (val, child) in enumerate(data_list):
            self.tree.move(child, "", index)

        # 정렬 상태 반전 설정
        self.tree.heading(col, command=lambda: self.sort_column(col, not reverse))

lst_frame1 = LabelFrame(combineframe1, text="PPT List")
lst_frame1.pack(side="left", padx=5, pady=5)
app = SortableTable(lst_frame1)

#selected ppt frame
slc_frame = LabelFrame(combineframe1, text="Selected Files")
slc_frame.pack(side="right", padx=5, pady=5, fill="y")

lstb_r = Listbox(slc_frame, height=5, selectmode="extended", width=43)
lstb_r.pack(fill="both", expand="True", padx=5, pady=5, side="left")

#btn ppt.
combineframe2 = Frame(slc_frame)
combineframe2.pack(side="right")
btn_slc_search = Button(combineframe2, text="설교 파일", width=10)
btn_slc_search.pack(padx=5, pady=5)
btn_slc_search = Button(combineframe2, text="설교 제거", width=10)
btn_slc_search.pack(padx=5, pady=5)
btn_slc_del = Button(combineframe2, text="선택 열기", width=10)
btn_slc_del.pack(padx=5, pady=5)
btn_slc_del = Button(combineframe2, text="선택 삭제", width=10)
btn_slc_del.pack(padx=5, pady=5)
lbl_pptframe = Label(combineframe2, text="")
lbl_pptframe.pack(padx=5, pady=5)
btn_slc_goup = Button(combineframe2, text="위로 이동", width=10)
btn_slc_goup.pack(padx=5, pady=5)
btn_slc_godown = Button(combineframe2, text="아래로 이동", width=10)
btn_slc_godown.pack(padx=5, pady=5)










#option frame
option_frame = LabelFrame(root, text="Option")
option_frame.pack(padx=5, pady=5, fill="x")

#1. 중간 슬라이드 개수 옵션
lbl_insslide = Label(option_frame, text="삽입슬라이드", width=10)
lbl_insslide.pack(padx=7, pady=7, side="left")

option_insslide = ["1개", "2개", "3개"]
cmb_insslide = ttk.Combobox(option_frame, state="readonly", values=option_insslide, width=10)
cmb_insslide.current(0)
cmb_insslide.pack(padx=7, pady=7, side="left")

#2. 우상단 워터마크 옵션
lbl_marking = Label(option_frame, text="워터마크", width=9)
lbl_marking.pack(side="left", padx=7, pady=7)

option_useornot = ["사용", "제거"]
cmb_marking = ttk.Combobox(option_frame, state="readonly", values=option_useornot, width=10)
cmb_marking.current(1)
cmb_marking.pack(side="left", padx=7, pady=7)

#3. 애니메이션 옵션
lbl_animation = Label(option_frame, text="에니매이션", width=9)
lbl_animation.pack(side="left", padx=7, pady=7)

cmb_animation = ttk.Combobox(option_frame, state="readonly", values=option_useornot, width=10)
cmb_animation.current(1)
cmb_animation.pack(side="left", padx=7, pady=7)

#4. 테마옵션
option_theme = ["기본테마", "테마1", "테마2"]
lbl_animation = Label(option_frame, text="테마선택", width=9)
lbl_animation.pack(side="left", padx=7, pady=7)

cmb_animation = ttk.Combobox(option_frame, state="readonly", values=option_theme, width=10)
cmb_animation.current(0)
cmb_animation.pack(side="left", padx=7, pady=7)


#progressbar frame
frame_progress = LabelFrame(root, text="Progress")
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