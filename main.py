import tkinter as tk
import pandas as pd
import random
import time
from tkinter import messagebox

# UI settings
BACKGROUND_C = "#FFE7BF"
FRAME_C = "#FFC4C4"
TITLE_C = "#A10035"
TEXT_C = "#525E75"
STOP_C = "#FF869E"
START_C = "#6CC4A1"

LABEL_FONT = ("Helvetica", 16, "bold")
TITLE_FONT = ("Helvetica", 30, "normal")
TEXT_FONT = ("Helvetica", 14, "normal")

# Functions


def clock(count):
    """ Shows time count after start button."""
    global timer
    count_min = int(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        timer_label["text"] = f"Timer: 0{count_min}:0{count_sec}"
    else:
        timer_label["text"] = f"Timer: 0{count_min}:{count_sec}"
    timer = window.after(1000, clock, count + 1)


def start_timer():
    """ Fixate start time and starts timer."""
    global start_time
    typing_text.delete("1.0", tk.END)
    count = 0
    start_time = time.time() #time in seconds
    start_button.config(bg="#FFE7BF")
    clock(0)


def calculate():
    """ Stops timer, calculates duration from start to stop, counts correct words and calculates final word count per minute."""
    finish_time = time.time()
    window.after_cancel(timer)
    total_correct_words = 0
    start_button.config(bg=START_C)
    typed_words = typing_text.get("1.0",tk.END).strip("\n")
    typed_words_list = typed_words.split(" ")

    for word_ind in range(0,len(typed_words_list)):
        if typed_words_list[word_ind] == random_words[word_ind]: # or change to if word in random words
            total_correct_words += 1
    durration_secs = finish_time - start_time
    words_per_min = round((total_correct_words / durration_secs * 60), 2)
    messagebox.showinfo(title="Words per minute", message=f"Your result is {words_per_min} words per minute. \nTotal"
                                                          f" correct words: {total_correct_words}")
    typing_text.delete("1.0", tk.END)
    timer_label["text"] = f"Timer: 00:00"


# get 50 random words from csv
all_words = pd.read_csv("word_list.csv", index_col=None, header=None)
word_list = all_words[0].to_list()
random_words = [random.choice(word_list) for n in range(50)]
words = " ".join(random_words)


# UI
window = tk.Tk()
window.title("Typing speed test")
window.minsize(500,500)
window.config(padx=50, pady=50,bg=BACKGROUND_C)

title = tk.Label(text="Typing speed test", bg=BACKGROUND_C, fg=TITLE_C, font=TITLE_FONT, justify='center')
title.grid(row=0, column=0, columnspan=3)

timer_label = tk.Label(text="Timer: 00:00", fg="#FF869E", font=LABEL_FONT, bg=BACKGROUND_C, justify="center")
timer_label.grid(row=1, column=0, columnspan=3)

words_label = tk.Label(text=words, bg=BACKGROUND_C, fg=TEXT_C, font=TEXT_FONT, wraplength=400, justify="center")
words_label.grid(row=2, column=0, columnspan=3)

typing_text = tk.Text(width=50, height=10, wrap="word")
typing_text.grid(row=4, column=0, columnspan=3)

start_button = tk.Button(text="START", bg=START_C, activebackground=START_C, fg=TITLE_C, activeforeground=TITLE_C,
                         font=LABEL_FONT, command=start_timer)
start_button.grid(row=5, column=0)
stop_button = tk.Button(text="STOP", bg=STOP_C, activebackground=STOP_C, fg=TITLE_C, activeforeground=TITLE_C,
                         font=LABEL_FONT, command=calculate)
stop_button.grid(row=5, column=2)
window.mainloop()
