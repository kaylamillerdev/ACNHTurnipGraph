import pypyodbc
import db_connection as dbConn

class Update:
    def func_UpdateEntry(self):
        # Get the sql connection
        connection = dbConn.getConnection()

        dateInput = input("For what date do you want to update a record? Please use the following format: mm-dd-yyyy OR yyyy-mm-dd: \n > ")
        nightOrDay = input("Which record do you want to update, AM or PM? \n > ")
        try:
            # Fetch the data which needs to be updated
            sql = "SELECT * FROM TurnipPriceData2 Where DateOfPrice = ? AND AM_PM = ?"
            cursor = connection.cursor()
            Values = [dateInput, nightOrDay]
            print(sql, Values)
            cursor.execute(sql, Values)
            entry = cursor.fetchone()
            menu = """
                    === Entry Found ===
            ------------------------------------
            """
            header = ('Data Fetched for Date: ', dateInput)
            print(menu)
            print(header)
            print('EntryID\t\t EntryID\t\t\t EntryDate \t\t\t TurnipPrice \t\t\t DateOfPrice \t\t\t AM_PM')
            print('-------------------------------------------')       
            print(' {}\t\t {} \t\t\t{} \t\t\t{} \t\t\t{} \t\t\t{} \t\t\t{}'.format(entry[0], entry[1], entry[2], entry[3], entry[4]))
            print('-------------------------------------------')
            print('Enter New Data To Update Turnpi Price Record ')

            TurnipPrice = input('Enter New Turnip Price: \n > ')
            newNightOrDay = input("Enter New Time of Day: (AM or PM): \n > ")
            convertedTurnipPrice = int(TurnipPrice)
        except:
            print("Something funky happened.")

        query = "UPDATE TurnipPriceData2 SET TurnipPrice = ?, AM_PM = ? where EntryID = item[0]"

        # Execute the update query
        cursor.execute(query, [convertedTurnipPrice, newNightOrDay])
        connection.commit()
        print('Entry Updated Successfully')
     
        # close the connection
        connection.close()