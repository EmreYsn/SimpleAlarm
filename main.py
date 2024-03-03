from tkinter import *
import time
import datetime
import os

def set_alarm():
    hour = int(entry_1.get())
    minute = int(entry_2.get())

    now = datetime.datetime.now()
    alarm_time = datetime.datetime.combine(now.date(),datetime.time(hour,minute))

    time.sleep((alarm_time - now).total_seconds())

    os.system("Start Alone")

window = Tk()
window.title("Alarm")
window.config(padx=75,pady=75)

label_1 = Label()
label_1.config(text="Set Hour")
label_1.pack()

entry_1 = Entry()
entry_1.config(width=30)
entry_1.pack()

label_2 = Label()
label_2.config(text="Set Minute")
label_2.pack()

entry_2 = Entry()
entry_2.config(width=30)
entry_2.pack()

button_1 = Button()
button_1.config(text="Set Time",command=set_alarm)
button_1.pack()

window.mainloop()