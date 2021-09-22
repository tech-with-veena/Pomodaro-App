from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timertext,text="00:00")
    title.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def starttimer():
    global reps
    reps+=1
    worksec=WORK_MIN * 60
    shortbreak=SHORT_BREAK_MIN *60
    longbreak=LONG_BREAK_MIN * 60
    if reps % 8 ==0:
        countdown(longbreak)
        title.config(text="Break",fg=RED)
    elif  reps % 2==0 :
        countdown(shortbreak)
        title.config(text="Break", fg=PINK)
    else:
        countdown(worksec)
        title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    countmin=math.floor(count/60)
    countsec=count%60
    if  countsec < 10 :
        countsec=f"0{countsec}"
    canvas.itemconfig(timertext,text=f"{countmin}:{countsec}")

    if count>0:
        global timer
        timer=window.after(1000,countdown,count-1)
    else:
        starttimer()
        mark=" "
        worksession=math.floor(reps / 2)
        for _ in range(worksession):
            mark += "✔"
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

title=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
title.grid(column=1,row=0)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomotoimage=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomotoimage,)
timertext=canvas.create_text(100,130,text="0:0",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

startbutton=Button(text="Start",highlightthickness=0,command=starttimer)
resetbutton=Button(text="Reset",highlightthickness=0,command=reset)
startbutton.grid(column=0,row=2)
resetbutton.grid(column=2,row=2)
checkmark=Label(fg=GREEN,bg=YELLOW)
checkmark.grid(column=1,row=3)







window.mainloop()
