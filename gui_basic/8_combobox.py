from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Gui Example")
root.geometry("640x480")

dateval = [str(i) + "일" for i in range(1,32)]
combobox = ttk.Combobox(root, height=5, values=dateval, state="readonly")
combobox.current(0)
combobox.pack()
combobox.set("카드 결제일")


def btncmd():
    print(combobox.get())


btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()