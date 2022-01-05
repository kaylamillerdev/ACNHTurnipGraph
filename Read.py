from pypyodbc import Cursor
import db_connection as dbConn
from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Read:
    def func_ReadEntries(self):
        def readAll():
            #Get the sql connection
            connection = dbConn.getConnection()
            cursor = connection.cursor()
            #Execute the sql query
            cursor.execute('SELECT DateOfPrice, AM_PM, TurnipPrice FROM TurnipPriceData2 ORDER BY DateOfPrice')
            menu = """=== Turnip Prices ===
            ------------------------------------"""
            print(menu)
            print(tabulate(cursor, headers=["Date of Price", "AM or PM", "Turnip Price"]))
            print('-------------------------------------------')
            connection.close()

        def func_GraphEntries():
            compiledXList = []
            #Get the sql connection
            connection = dbConn.getConnection()
            cursor = connection.cursor()

            #Execute the sql query
            cursor.execute('SELECT ConcatDateAMPM, TurnipPrice, DateOfPrice FROM TurnipPriceData2 Order By DateOfPrice')
            data = cursor.fetchall()
            data = list(zip(*data))

            #print("Data 1: ", data[1])
            #print("Data 0: ", data[0])

            dataList1 = list(data[0])
            dataList2 = list(data[1])
            
            
            
            xpoints = np.array(data[0])
            ypoints = np.array(data[1])
            plt.xticks(rotation=90)
            plt.plot(xpoints, ypoints, 'o-m')
            plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
            plt.title("Turnip Data Graph")
            plt.xlabel("Dates")
            plt.ylabel("Prices")
            plt.show()
            # Print the Data
            """for row in cursor:
                #print('row = %r' % (row,))
                #print(*row, sep=" ")
                for field in row:
                    print(field)
                    
                    print(xpoints)
            connection.close() """
        readAll()
        func_GraphEntries()