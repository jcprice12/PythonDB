import sys
import mysql.connector
from mysql.connector import errorcode
from datetime import date
from passlib.hash import pbkdf2_sha256
import utils.validator as validator
import utils.queries as queries
import prompts.editUser as editUser
import prompts.createUser as createUser
import prompts.browse as browse

#Pretty much the main menu screen for a customer once they have logged in
#Decide whether or not to print out your orders, purchase clothing, or edit your personal info
def customerAction(connection, custID):
    customerInteracting = True
    while customerInteracting == True:
        leInput = raw_input("""\nWelcome to the action screen. Input an action or type 'back' to go back\nView Orders (0)\nView Clothing & Place Order (1)\nEdit Your Account (2)\n""")
        if leInput == "back":
            customerInteracting = False
        elif leInput == "0":
			queries.printOrders(connection, (custID,))
        elif leInput == "1":
            browse.viewAndPlace(connection, custID)
        elif leInput == "2":
            editUser.editAccount(connection,custID)

#This is the starting point of my program. The program attempts to connect to the database. Once it has, it will prompt the user to "log in"
#by entering their Customer ID and password. If they don't have an account they must make one to access any of the functionality of this program.           
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
					print("That's an invalid password format")

			customer = queries.getCustomer(connection, (custId,))
			if customer != None:
				if pbkdf2_sha256.verify(custPass, customer[9]):
					newCustID = customer[0]
					customerAction(connection, newCustID)
				else:
					print("INVALID PASSWORD")
			else:
				print("INVALID USER ID")
except mysql.connector.Error as err:
    print("Something went wrong: {}".format(err))
else:
    connection.close()
