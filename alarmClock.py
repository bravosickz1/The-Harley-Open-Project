import datetime 
from playsound import playsound
from rem2 import rem

#user inputs
alarmHour = int(input("Please set your alarm time(HH) : "))
alarmMinute = int(input("Please set your alarm time(MM) : "))
AmPm = input("am/pm : ")

#12 hour format
if AmPm == "pm":
    alarmHour += 12
#confirmation message
print("Alarm set for ", alarmHour,":", alarmMinute)

#setting the alarm
while True:
    if alarmHour == datetime.datetime.now().hour:
        if alarmMinute == datetime.datetime.now().minute:
            rem("Your Alarm's ringing!")
            playsound("Seirei.mp3")
