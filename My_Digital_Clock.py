from tkinter import *
import time
from datetime import date
from datetime import datetime

#Step1: setting window screen

window = Tk()
window.geometry("500x500")
window.title("Digital Clock")

#step:5 defining date function

def current_date():
    today = date.today()
    #for textual month, give below format
    today_date = today.strftime("%B %d, %Y")
    date_label.config(text=f"Today is : {today_date}")

#step 4: creating date label
date_label = Label(window, font=("roman", 20, "bold"), fg="steel blue", bg="pink", width="30")
date_label.pack(pady="60")

#step3: defining function for digital clock configuration
def digital_clock():
    now = datetime.now()
    get_time = now.strftime("%H:%M:%S")
    #get_time = time.strftime("%H:%M:%S %p")
    clock_label.config(text=f"Time is : {get_time}")
    clock_label.after(1000, digital_clock) #purpose?

# Step2: Creating label for digital clock

clock_label = Label(window, font=("roman", 20, "bold"), fg="steel blue", bg="pink", width="20")
clock_label.pack(pady="20")

digital_clock()
current_date()
window.mainloop()
