from tkinter import *
import math
#------CONSTANTS----------
PINK = "#FFF1E6"
RED =  "#C1121F"
GREEN = "#386641"  
YELLOW = "#FAEDCD"
TEXT = "#334155" 
FONT_NAME = "Helvetica"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#-------TIMER RESET---------------
#--------TIMER MECHANISM---------
def start_timer():
    count_down(5*60)


#-------COUNTDOWN MECHANISM---------
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    canvas.itemconfig(timer_text,text=f"{count_min} : {count_sec}")
    if count > 0:
        window.after(1000,count_down,count-1)




#---------UI SETUP------------
window =Tk()
window.title("Pomodoro")
window.config(padx=50, pady=20, bg=YELLOW)




timer = Label(text="Timer",fg=GREEN,bg=YELLOW, font=(FONT_NAME,42,"bold"),)
timer.grid(column=1, row=0)

canvas=Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="d:/Python/tkinter/day_28/tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00" ,fill="white", font=(FONT_NAME,42,"bold"))
canvas.grid(column=1, row=1)



start=Button(text="Start", highlightthickness=0,command=start_timer)
start.grid(column=0, row=2)

reset=Button(text="Reset",highlightthickness=0)
reset.grid(column=2, row=2)

check_marks = Label(text="✓" ,fg=GREEN, bg=YELLOW,font=(FONT_NAME,42,"bold"))
check_marks.grid(column=1,row=3)



window.mainloop()