import pypyodbc
import db_connection as dbConn
from tabulate import tabulate
import re

class Delete:
    def func_DeleteEntry(self):
        
        def getAllEntries():
            # Get the sql connection
            connection = dbConn.getConnection()
            cursor = connection.cursor()
            #Execute the sql query
            cursor.execute('SELECT * FROM TurnipPriceData2 Order By EntryID')
            
            
            print(tabulate(cursor, headers=["EntryID", "Date Entry was Made", "Turnip Price", "Date of Price", "AM or PM", "Turnip Price"]))
         
            connection.close()

        def deleteOne():
            userChoice = input("Choose the ID for the entry you want to delete: \n >")
            userChoice = int(userChoice)
            # Get the sql connection
            connection = dbConn.getConnection()
            cursor = connection.cursor()
            query = 'DELETE FROM TurnipPriceData2 WHERE EntryID = ?'
            #Execute the sql query
            cursor.execute(query, [userChoice])
            connection.commit()
            print('Entry Deleted Successfully')
            connection.close()
       
        getAllEntries()
        deleteOne()
        userInput = input("Do you want to delete more entries? \n >")
        if (userInput == re.Match("^[nN]")):
            quit()
        elif (userInput == re.Match("^[yY]")):
            deleteOne()