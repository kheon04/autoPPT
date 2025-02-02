import tkinter as tk
from tkinter import ttk

class SortableTable:
    def __init__(self, root):
        # self.root = root
        # self.root.title("Sortable Table Example")

        # Treeview 설정
        # columns = [(이름, width), ]
        self.columns = [("SongID", 50), ("아티스트", 80), ("이름", 200), ("수정한 날짜", 150), ("만든 날짜", 150)]
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


if __name__ == "__main__":
    root = tk.Tk()
    app = SortableTable(root)
    root.mainloop()
