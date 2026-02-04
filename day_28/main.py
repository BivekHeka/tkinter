from tkinter import *
import math

# ------ COLORS & FONT ----------
BG = "#FFF8F1"          # warm cream background
PRIMARY = "#2F6F5E"     # calm green (work)
ACCENT = "#E3644A"      # coral (breaks)
SOFT = "#9CA3AF"        # muted gray (short break)
TEXT = "#2E2E2E"
RED = "#C1121F"
FONT_NAME = "Poppins"   # more modern and attractive

WORK_MIN = 30 
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = None
reps = 0

# ------- TIMER RESET ---------------
def timer_reset():
    global reps, timer
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=TEXT)
    check_marks.config(text="")
    reps = 0

# -------- TIMER MECHANISM ---------
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED, font=(FONT_NAME, 32, "bold"))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=ACCENT, font=(FONT_NAME, 32, "bold"))
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=PRIMARY, font=(FONT_NAME, 32, "bold"))

# ------- COUNTDOWN MECHANISM ---------
def count_down(count):
    global timer
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)

# --------- UI SETUP ------------
window = Tk()
window.title("Pomodoro Timer")
window.config(bg=BG, padx=60, pady=30)
window.resizable(False, False)

# ---- TITLE ----
title_label = Label(
    text="Timer",
    fg=TEXT,
    bg=BG,
    font=(FONT_NAME, 32, "bold"),
    anchor="center"
)
title_label.grid(column=1, row=0, pady=(0, 15))

# ---- CANVAS ----
canvas = Canvas(width=200, height=200, bg=BG, highlightthickness=0)
tomato_img = PhotoImage(file="d:/Python/tkinter/day_28/tomato.png")
canvas.create_image(100, 100, image=tomato_img)
timer_text = canvas.create_text(
    100, 110,
    text="00:00",
    fill="white",
    font=(FONT_NAME, 28, "bold")
)
canvas.grid(column=1, row=1, pady=(0, 15))

# ---- BUTTONS ----
button_style = {
    "font": (FONT_NAME, 12, "bold"),
    "fg": "white",
    "bd": 0,
    "padx": 16,
    "pady": 6,
    "cursor": "hand2",
}

start = Button(text="Start", command=start_timer, bg=PRIMARY, **button_style)
start.grid(column=0, row=2, padx=10, pady=10)

reset = Button(text="Reset", command=timer_reset, bg=ACCENT, **button_style)
reset.grid(column=2, row=2, padx=10, pady=10)

# ---- CHECK MARKS ----
check_marks = Label(fg=PRIMARY, bg=BG, font=(FONT_NAME, 24, "bold"))
check_marks.grid(column=1, row=3, pady=(10,0))

window.mainloop()
