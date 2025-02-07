import tkinter as tk
from tkinter import ttk

# class PlaceholderEntry(tk.Entry):
#     """
#     Entry에 임의로 Placeholder를 추가합니다.
#     PlaceholderEntry(root, placeholder="Enter sth...", color="grey")
    
#     """
#     def __init__(self, master=None, placeholder="Enter sth...", color="grey"):
#         super().__init__(master)

#         self.placeholder = placeholder
#         self.placeholder_color = color
#         self.default_fg_color = self['fg']

#         self.insert(0, self.placeholder)
#         self['fg'] = self.placeholder_color

#         self.bind("<FocusIn>", self._clear_placeholder)
#         self.bind("<FocusOut>", self._add_placeholder)

#     def _clear_placeholder(self, event):
#         if self.get() == self.placeholder:
#             self.delete(0, "end")
#             self['fg'] = self.default_fg_color

#     def _add_placeholder(self, event):
#         if not self.get():
#             self.insert(0, self.placeholder)
#             self['fg'] = self.placeholder_color
class PlaceholderEntry(tk.Entry):
    """
    Entry에 임의로 Placeholder를 추가합니다.
    PlaceholderText(root, placeholder="Enter sth...", color="grey", ...)
    
    """
    def __init__(self, master=None, placeholder="Type here...", color="grey"):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)

        # Enter 키 이벤트 바인딩
        self.bind("<Return>", self._on_enter_pressed)

    def _clear_placeholder(self, event):
        if self.get() == self.placeholder:
            self.delete(0, "end")
            self['fg'] = self.default_fg_color

    def _add_placeholder(self, event):
        if not self.get():
            self.insert(0, self.placeholder)
            self['fg'] = self.placeholder_color

    def _on_enter_pressed(self, event):
        user_input = self.get()
        self.perform_action(user_input)

    def perform_action(self, text):
        """
        사용자 입력 처리 함수 (필요 시 커스터마이징)
        def custom_action(text): ...
        entry.perform_action = custom_action
        """
        print(f"Action did not assigned! input: '{text}'")
        
class PlaceholderText(tk.Text):
    
    def __init__(self, master=None, placeholder="Enter sth...", color="grey", **kwargs):
        super().__init__(master, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg'] if 'fg' in kwargs else "black"

        # 플레이스홀더 초기 설정
        self._add_placeholder()
        
        # 이벤트 바인딩
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)

    def _clear_placeholder(self, event=None):
        if self.get("1.0", "end-1c") == self.placeholder:
            self.delete("1.0", "end")
            self['fg'] = self.default_fg_color

    def _add_placeholder(self, event=None):
        if not self.get("1.0", "end-1c").strip():
            self.insert("1.0", self.placeholder)
            self['fg'] = self.placeholder_color


class SortableTable:
    def __init__(self, root):
        # self.root = root
        # self.root.title("Sortable Table Example")

        # Treeview 설정
        # columns = [(이름, width), ]
        self.columns = [("ID", 60), ("아티스트", 120), ("이름", 250), ("수정한 날짜", 150),("섹션 분리", 70)]
        column_names = [col[0] for col in self.columns]
        self.tree = ttk.Treeview(root, columns=column_names, show='headings')

        # 각 컬럼 헤더와 넓이, 정렬 설정
        for col in self.columns:
            self.tree.heading(col[0], text=col[0], command=lambda c=col[0]: self.sort_column(c, False))
            self.tree.column(col[0], width=col[1], anchor=tk.CENTER)

        # packing
        self.tree.pack(fill=tk.BOTH, expand=True, pady=5, padx=5)

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