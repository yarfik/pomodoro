import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 3 #25
SHORT_BREAK_MIN = 2  #5
LONG_BREAK_MIN = 1 #20
CHECKMARK = "☑"
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global REPS, TIMER

    REPS = 0
    canvas.itemconfig(txt_timer, text="00:00")
    lbl_timer.config(text="Timer")
    lbl_checkmark.config(text="")
    root.after_cancel(TIMER)

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS

    REPS += 1
    if REPS == 8:
        count_down(LONG_BREAK_MIN * 60)
        lbl_timer.config(text="Break", fg=RED)
        REPS = 0
    elif REPS % 2 == 0:
        lbl_timer.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        lbl_timer.config(text="WORK", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global TIMER, REPS

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(txt_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        TIMER = root.after(100, count_down, count - 1)
    else:
        marks = ""
        for _ in range(math.floor(REPS/2)):
            marks += CHECKMARK

        lbl_checkmark.config(text=marks)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


root = tk.Tk()
root.title("Podomoro")
root.config(padx=100, pady=50, bg=YELLOW)

# title
lbl_timer = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "normal"))
lbl_timer.grid(column=1, row=0)

# tomato
tomato_img = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)

# timer
txt_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# buttons
btn_start = tk.Button(text="Start", bg=YELLOW, fg=RED, highlightthickness=0, font=(FONT_NAME, 12, "bold"))
btn_start.grid(column=0, row=2)
btn_start.config(command=start_timer)

btn_reset = tk.Button(text="Reset", bg=YELLOW, fg=RED, highlightthickness=0, font=(FONT_NAME, 12, "bold"))
btn_reset.grid(column=2, row=2)
btn_reset.config(command=reset_timer)

# checkmark
lbl_checkmark = tk.Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
lbl_checkmark.grid(column=1, row=3)

root.mainloop()