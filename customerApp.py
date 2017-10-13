import sys
import mysql.connector
from mysql.connector import errorcode
from datetime import date
import validator
import editUser
import createUser
import browse

#Pretty much the main menu screen for a customer once they have logged in
#Decide whether or not to print out your orders, purchase clothing, or edit your personal info
###########################################################################################################################
def customerAction(connection, custID):
    customerInteracting = True
    while customerInteracting == True:
        leInput = raw_input("""\nWelcome to the action screen. Input an action or type 'back' to go back\nView Orders (0)\nView Clothing & Place Order (1)\nEdit Your Account (2)\n""")
        if leInput == "back":
            customerInteracting = False
        elif leInput == "0":
            cursor = connection.cursor()
            SQL = """   select InvoiceLineID, ClothingID, Name, SoldFor, Credit
                        from (JohmpsonClothing.Clothing natural join JohmpsonClothing.InvoiceLine) natural join JohmpsonClothing.Invoice
                        where CustomerID = """ + str(custID) + """;"""
            cursor.execute( SQL )
            print("{0:10}{1:12}{2:2}{3:20}{4:10}{5:32}".format("Line Id", "Clothing ID", "", "Name", "Sold For", "Credit Card"))
            for (InvoiceLineId, ClothingId, Name, SoldFor, Credit) in cursor:
                print("{0:10}{1:12}{2:2}{3:20}${4:10}{5:32}".format(str(InvoiceLineId), str(ClothingId), " ", Name, str(SoldFor), Credit))
            cursor.close()
        elif leInput == "1":
            cursor = connection.cursor()
            cursor.execute("""  select max(InvoiceID)
                                from Invoice""")
            maxID = cursor.fetchone()
            cursor.close()
            inID = maxID[0] + 1
            browse.viewAndPlace(connection, custID, inID)
        elif leInput == "2":
            editUser.editAccount(connection,custID)

#This is the starting point of my program. The program attempts to connect to the database. Once it has, it will prompt the user to "log in"
#by entering their Customer ID and password. If they don't have an account they must make one to access any of the functionality of this program.
###########################################################################################################################            
try: 
    connection = mysql.connector.connect(host='127.0.0.1', user='root', password='password', database='JohmpsonClothing')
    appRunning = True
    while appRunning == True:
        print("\nWelcome to the main screen, type 'q' to exit the application or your user id to continue")
        print("New to Johmpson Clothing? Create an acount by typing 'new'.")
        isValid = False
        while isValid == False:
            custId = raw_input()
            try:
                if custId == "new" or custId == "q":
                    isValid = True
                else:
                    cust = int(custId)
                    isValid = True
            except:
                print("That's an invalid customer ID")
        if custId == "q":
            appRunning = False
        elif custId == "new":
            createUser.customerRegistration(connection)
        else:
            isValid = False
            while isValid == False:
                print("Please type in your password or type 'exit' to exit")
                custPass = raw_input()
                if validator.validatePass(custPass):
                    isValid = True
                else:
                    print("That's an invalid password")
            else:
                cursor = connection.cursor()
                SQL = ("""SELECT CustomerID
                            FROM Customer
                            WHERE CustomerID = %s and Password = %s;""")
                data = (custId,custPass)
                cursor.execute(SQL, data)
                customer = cursor.fetchone()
                cursor.close()
                if customer != None:
                    newCustID = customer[0]
                    customerAction(connection, newCustID)
                else:
                    print("INVALID USER ID OR PASSWORD\n")
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
else:
    connection.close()
