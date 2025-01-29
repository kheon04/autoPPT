from tkinter import *

root = Tk()
root.title("Gui Example")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(width=10, height=3, text="버튼3")
btn3.pack()

btn4 = Button(root, fg="red", bg="yellow", text="버튼4")
btn4.pack()

checkbox_button = PhotoImage(file="gui_basic/src/checkbox.png")

btn5 = Button(root, image=checkbox_button)
btn5.pack()

def btncmd():
    print("동작중임")

btn6 = Button(root, text="동작버튼", command=btncmd)
btn6.pack()








root.mainloop()