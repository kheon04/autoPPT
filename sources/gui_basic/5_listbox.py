from tkinter import *

root = Tk()
root.title("Gui Example")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=3)
listbox.insert(0,"사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
    # listbox.delete(END)
    # print("1 to 3: ", listbox.get(0,2))
    print("now : ", listbox.curselection()) #위치형태의 list로 변환


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()