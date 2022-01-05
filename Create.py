from typing import Match
import pypyodbc
import time
import datetime
import datePicker
import db_connection as dbConn
import re
class Create:
    # self is equal to the 'this' keyword in JS
    def func_CreateEntry(self):
        # Create some functions
        def createAnEntry():
            inputDate = ""
            inputDate = input("Please input the date you wish to record a turnip price for: \n\n > ")
            inputDate = datetime.datetime.strptime(inputDate, "%m/%d/%Y")

            if(inputDate > datetime.datetime.now()):
                print("Invalid date! Turnip prices cannot be known in advance. Please try again! \n")
                createAnEntry()
            elif(inputDate < datetime.datetime.now()):
                inputDate
            else:
                print("This date is today's date!")
                response = input("Did you mean to choose today's date? \n > ")
                if(response == re.Match("^[nN]")):
                    print("Please choose a different date!")
                    dateSelection()
                elif(response == re.Match("^[yY]")):
                    inputDate
      
            dayOrNight = input("Is this entry for AM or PM? \n > ")
            Weekday = inputDate.strftime("%A")
            print("Weekday: ", Weekday)
            concatDateAMPM = Weekday + " " + inputDate.strftime("%Y-#m-%d") + " " + dayOrNight
            print("xLabel: ", concatDateAMPM)

            enteredPrice = input('Enter the price for turnips on that date \n >')
            try:
                enteredPrice = int(enteredPrice)
                query = "INSERT INTO TurnipPriceData2(TurnipPrice, DateOfPrice, AM_PM, ConcatDateAMPM, Weekday) VALUES(?,?,?,?,?);"
            except:
                print('Something is wrong. Please try again!')

            connection = dbConn.getConnection()
            Values = [enteredPrice, inputDate, dayOrNight, concatDateAMPM, Weekday]
            cursor = connection.cursor()

            #  Execute the sql query
            cursor.execute(query, Values)
            # commit the data
            connection.commit()
            print('Data saved successfully')
         
            connection.close()
            moreData = input("Would you like to enter another data point?: (y/n) \n >")
            if(moreData == "y"):
                createAnEntry()
            else:
                print("Goodbye!")
                quit()

        createAnEntry()