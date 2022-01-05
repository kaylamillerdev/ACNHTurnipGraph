from Create import Create
from Read import Read
from Update import Update
from Delete import Delete
from pyfiglet import Figlet

class Main:

    print(
        """

     /$$$$$$$$                            /$$                  /$$$$$$                               /$$       /$$                    
    |__  $$__/                           |__/                 /$$__  $$                             | $$      |__/                    
       | $$ /$$   /$$  /$$$$$$  /$$$$$$$  /$$  /$$$$$$       | $$  \__/  /$$$$$$  /$$$$$$   /$$$$$$ | $$$$$$$  /$$ /$$$$$$$   /$$$$$$ 
       | $$| $$  | $$ /$$__  $$| $$__  $$| $$ /$$__  $$      | $$ /$$$$ /$$__  $$|____  $$ /$$__  $$| $$__  $$| $$| $$__  $$ /$$__  $$
       | $$| $$  | $$| $$  \__/| $$  \ $$| $$| $$  \ $$      | $$|_  $$| $$  \__/ /$$$$$$$| $$  \ $$| $$  \ $$| $$| $$  \ $$| $$  \ $$
       | $$| $$  | $$| $$      | $$  | $$| $$| $$  | $$      | $$  \ $$| $$      /$$__  $$| $$  | $$| $$  | $$| $$| $$  | $$| $$  | $$
       | $$|  $$$$$$/| $$      | $$  | $$| $$| $$$$$$$/      |  $$$$$$/| $$     |  $$$$$$$| $$$$$$$/| $$  | $$| $$| $$  | $$|  $$$$$$$
       |__/ \______/ |__/      |__/  |__/|__/| $$____/        \______/ |__/      \_______/| $$____/ |__/  |__/|__/|__/  |__/ \____  $$
                                             | $$                                         | $$                               /$$  \ $$
                                             | $$                                         | $$                              |  $$$$$$/
                                             |__/                                         |__/                               \______/ 
                              /$$$$$$            /$$                     /$$             /$$                                          
                             /$$__  $$          | $$                    | $$            | $$                                          
                            | $$  \__/  /$$$$$$ | $$  /$$$$$$$ /$$   /$$| $$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$                   
                            | $$       |____  $$| $$ /$$_____/| $$  | $$| $$ |____  $$|_  $$_/   /$$__  $$ /$$__  $$                  
                            | $$        /$$$$$$$| $$| $$      | $$  | $$| $$  /$$$$$$$  | $$    | $$  \ $$| $$  \__/                  
                            | $$    $$ /$$__  $$| $$| $$      | $$  | $$| $$ /$$__  $$  | $$ /$$| $$  | $$| $$                        
                            |  $$$$$$/|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$                        
                             \______/  \_______/|__/ \_______/ \______/ |__/ \_______/   \___/   \______/ |__/                        
                                                                                                                                  
                                                                                                                                  
                                                                                                                                  
            """
                                                                                                                                                                        
    )
    def mainMenu():
        print("\n\nWelcome! \n Please Choose an Option: \n ")
        choice = input(" 1) See Currently Saved Entries \n 2) Create An Entry \n 3) Update A Past Entry \n 4) Delete a Past Entry \n \n > ")
        ci = int(choice)

        if ci == 1:
            # Read turnip data
            readObj = Read()
            readObj.func_ReadEntries()

        if ci == 2:
            # Create an entry
            createObj = Create()
            createObj.func_CreateEntry()

        if ci == 3:
            # update an entry
            updateObj = Update()
            updateObj.func_UpdateEntry()
        if ci == 4:
            # Delete an entry
            deleteObj = Delete()
            deleteObj.func_DeleteEntry()
    mainMenu()