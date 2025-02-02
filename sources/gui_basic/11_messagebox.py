from tkinter import *
import tkinter.messagebox as msgbox


root = Tk()
root.title("Gui Example")
root.geometry("640x480")

#기차 예매 시스템이라고 가정
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")
def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")
def error():
    msgbox.showerror("Error", "결제 오류가 발생했습니다.") 
def okcancel():
    msgbox.askokcancel("Seoul Metro", "해당 좌석으로 예매를 완료하시겠습니까?") #확인 취소
def retrycancel():
    global errorcode
    errorcode = 10
    msgbox.askretrycancel("Seoul Metro", "일시적인 오류입니다.\nError code:%d"% errorcode) #다시시도 취소
def yesno():
    response = msgbox.askyesno("예 / 아니오", "역방향으로 예매합니까?") 
    if response == 1:
        print("예")
    if response == 0:
        print("아니오")  
def yesnocancel():
    response = msgbox.askyesnocancel(None, "예매 내역이 저장되지 않았습니다. \n저장 후 프로그램을 종료하시겠습니까?") 
    # print("응답:", response) #True, False, None -> 예:1, 아니오:0, 취소:else
    if response == 1:
        print("예")
    if response == 0:
        print("아니오")  
    else:
        print("취소")  


Button(root, text= "알림", command=info).pack()
Button(root, text= "경고", command=warn).pack()
Button(root, text= "Error", command=error).pack()
Button(root, text= "완료", command=okcancel).pack()
Button(root, text= "완료", command=retrycancel).pack()
Button(root, text= "예/아니오", command=yesno).pack()
Button(root, text= "예아니오취소", command=yesnocancel).pack()



root.mainloop()
