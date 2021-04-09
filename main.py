# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import winsound
import time
from win10toast_click import ToastNotifier

snooze_count=0

def callback_fun():
    global snooze_count
    snooze_count += 1
    print("Snooze count : " + str(snooze_count))


def fun(reminder, secs):

    notificator = ToastNotifier()
    # notificator.show_toast("Reminder",f"""Alarm will go off in {secs} secs""",duration=secs)
    if snooze_count == 0:
        #First Snooze take necessary actions
        notificator.show_toast("Reminder",f"{reminder} \n Click to snooze",duration=secs,callback_on_click=callback_fun)
    if snooze_count == 1:
        #Second Snooze take necessary actions
        notificator.show_toast("Reminder",f"{reminder} \n Click to snooze",duration=secs,callback_on_click=callback_fun)
    if snooze_count == 2:
        #Third Snooze take necessary actions
        notificator.show_toast("Reminder",f"{reminder} \n Click to snooze",duration=secs,callback_on_click=callback_fun)

    #Alarm
    frequency=2500
    duration=1000
    winsound.Beep(frequency,duration)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = input("Enter the reminder message")
    sec = int(input("Enter seconds"))

    while True:
        fun(words, sec)
        #Sleep for 15 mins
        time.sleep(15*60)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
