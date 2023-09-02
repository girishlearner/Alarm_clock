from tkinter import *
from tkinter import messagebox as msgbx
import datetime as dt
import time
from tkinter.ttk import Combobox

import winsound as ws
import os


def alarm(setAlarmTimer):
    while True:
        time.sleep(1)
        actualTime = dt.datetime.now()
        currentTime = actualTime.strftime("%H : %M : %S")
        currentDate = actualTime.strftime("%d / %m / %Y")
        the_message = "Current Time: " + str(currentTime + ",Given Time:  " + str(setAlarmTimer))
        print(the_message)
        if currentTime == setAlarmTimer:
            ws.PlaySound("ringtones/ring9.wav", ws.SND_ASYNC)
            msgbx.showinfo("Alert","It is time to wake up")
            break


def getAlarmTime():
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"
    alarm(alarmSetTime)


guiWindow = Tk()
guiWindow.title("Alarm Clock")
guiWindow.geometry("600x350")
guiWindow.config(bg="#6F88FA")
guiWindow.resizable(width=False, height=False)


add_time = Label(
    guiWindow, text="Hour  :  Minute  :  Second", font=("Times",16,"bold"), fg="black",bg="white"
).place(x=180, y=100)

add_title=Label(
    guiWindow,text="ALARM CLOCK",font=("Times",20,"bold"),bg="#66FAF1",fg="black"
).place_configure(x=200,y=20)


setAlarm = Label(
    guiWindow,
    text="Set Time: ",
    fg="black",
    bg="#1FBD06",
    width=9,
    font=("Times", 14, "bold"),
).place(x=50, y=150)

hour = StringVar(guiWindow)
minute = StringVar(guiWindow)
second = StringVar(guiWindow)

list2 = list(range(1,25))
hourTime = Combobox(guiWindow, values= list2,textvariable=hour, width=2, font=(20))
hourTime.place(x=180, y=150)



minuteTime = Combobox(guiWindow,textvariable=minute,width=2, font=(20))
minuteTime['values'] = ('00','01','02','03','04','05','06','07','08','09','10',
                        '11','12','13','14','15','16','17','18','19','20',
                        '21','22','23','24','25','26','27','28','29','30',
                        '31','32','33','34','35','36','37','38','39','40',
                        '41','42','43','44','45','46','47','48','49','50',
                        '51','52','53','54','55','56','57','58','59','60')
minuteTime.place(x=260, y=150)
secondTime = Combobox(guiWindow,textvariable=second,width=2, font=(20))
secondTime['values'] = minuteTime['values'] = ('00','01','02','03','04','05','06','07','08','09','10',
                        '11','12','13','14','15','16','17','18','19','20',
                        '21','22','23','24','25','26','27','28','29','30',
                        '31','32','33','34','35','36','37','38','39','40',
                        '41','42','43','44','45','46','47','48','49','50',
                        '51','52','53','54','55','56','57','58','59','60')
secondTime.place(x=350, y=150)

submit = Button(
    guiWindow,
    text="Set Alarm",
    fg="black",
    font=("Times",14,"bold"),
    bg="#C5FF01",
    width=14,
    command=getAlarmTime,
).place(x=180, y=220)

add = Label(
    guiWindow, text="Remember to enter time in 24 hour format", font=("Times",16,"bold"), fg="black",bg="white"
).place(x=100, y=300)


guiWindow.mainloop()
