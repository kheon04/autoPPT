from tkinter import *

root = Tk()
root.title("Gui Example")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")


#login id 등을 받을때는 entry를 이용
e = Entry(root, width=30)
e.pack()
e.insert(0, "한줄만 입력하세요.")


def btncmd():
    print(txt.get("1.0",END))  #1: 첫째라인, 0:0번째 column위치
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()