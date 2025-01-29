import tkinter as tk
from tkinter import ttk

def create_table_ui():
    # 메인 윈도우 생성
    root = tk.Tk()
    root.title("Song Table UI Example")

    # Treeview 설정
    columns = ("SongID", "Artist", "Name", "수정된 날짜", "만든 날짜")
    tree = ttk.Treeview(root, columns=columns, show='headings')

     # 각 컬럼 헤더와 넓이, 정렬 설정
    tree.heading("SongID", text="SongID")
    tree.column("SongID", width=50, anchor=tk.CENTER)

    tree.heading("Artist", text="ArtistID")
    tree.column("Artist", width=80, anchor=tk.CENTER)

    tree.heading("Name", text="Name")
    tree.column("Name", width=200, anchor=tk.W)  # 왼쪽 정렬

    tree.heading("수정된 날짜", text="수정된 날짜")
    tree.column("수정된 날짜", width=150, anchor=tk.CENTER)

    tree.heading("만든 날짜", text="만든 날짜")
    tree.column("만든 날짜", width=150, anchor=tk.CENTER)

        # 데이터 삽입
    sample_data = [
        (1, "NULL", "Born Again", "2025-01-29 17:26:13", "2025-01-29 17:26:13"),
        (2, "1001", "Dreams Alive", "2023-11-21 10:15:12", "2023-11-20 09:00:00"),
        (3, "1002", "Skyward", "2024-02-03 12:05:30", "2024-02-03 11:45:15")
    ]
    # 행 색상 변경 (구분선 느낌)
    for i, row in enumerate(sample_data):
        tag = "evenrow" if i % 2 == 0 else "oddrow"
        tree.insert("", tk.END, values=row, tags=(tag,))

    # 행 스타일 설정
    tree.tag_configure("evenrow", background="#f0f0f0")
    tree.tag_configure("oddrow", background="#ffffff")

    tree.pack(fill=tk.BOTH, expand=True)

    # 실행
    root.mainloop()

class SortableTable:
    def __init__(self, root):
        self.root = root
        self.root.title("Sortable Table Example")

        # 테이블 컬럼 정의
        self.columns = ("SongID", "ArtistID", "Name", "Modified Date", "Made Date")
        self.tree = ttk.Treeview(root, columns=self.columns, show="headings")

        # 컬럼 헤더 및 넓이 설정
        for col in self.columns:
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_column(c, False))
            self.tree.column(col, width=150, anchor=tk.CENTER)

        # 데이터 예제
        self.data = [
            (1, "NULL", "Born Again", "2025-01-29 17:26:13", "2025-01-29 17:26:13"),
            (2, "1001", "Dreams Alive", "2023-11-21 10:15:12", "2023-11-20 09:00:00"),
            (3, "1002", "Skyward", "2024-02-03 12:05:30", "2024-02-03 11:45:15")
        ]

        # 초기 데이터 삽입
        self.populate_table(self.data)

        self.tree.pack(fill=tk.BOTH, expand=True)

    def populate_table(self, data):
        # 기존 데이터 삭제
        for row in self.tree.get_children():
            self.tree.delete(row)

        # 정렬된 데이터 삽입
        for row in data:
            self.tree.insert("", tk.END, values=row)

    def sort_column(self, col, reverse):
        # 정렬 로직
        idx = self.columns.index(col)
        sorted_data = sorted(self.data, key=lambda x: x[idx], reverse=reverse)

        # 테이블 갱신
        self.populate_table(sorted_data)

        # 정렬 상태 반전
        self.tree.heading(col, command=lambda: self.sort_column(col, not reverse))


if __name__ == "__main__":
    root = tk.Tk()
    app = SortableTable(root)
    root.mainloop()
