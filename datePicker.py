from tkinter import *
from tkcalendar import Calendar
import datetime

def getPrettyTodaysDate():
    unformattedDate = datetime.datetime.now()
    #Weekday Month Name (short version), numerical day, full year, AM/PM
    finalDate = unformattedDate.strftime("%a %b %d %Y %p")
    print(finalDate)
    return finalDate

def getTodaysDate():
    unformattedDate = datetime.datetime.now()
    return unformattedDate
    finalDate = unformattedDate.strftime("%m/%d/%Y")
    #print("Today's Date: ", finalDate)
    #return finalDate