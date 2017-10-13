import validator
import createUser
import queries

def editFirstName(connection, custID, compare):
	isValid = False
    while isValid == False:      
        first = raw_input("Please enter your new first name:\n")
        if len(first) > 0 and len(first) < 46 and validator.validateStr(first):
            isValid = True
		else:
			print("Invalid Name")

    isValid = False
    while isValid == False:
        secret = raw_input("Enter your password")
        if secret == compare:
            isValid = True
        else:
            print("Sorry, wrong password")

	data = (first,custID)
	if queries.updateCustomerFirstName(connection, data) is None:
		print("Unable to update your name. Please try again")

def editLastName(connection, custID, compare):
    isValid = False
    while isValid == False:     
        last = raw_input("Please enter your last name:\n")
        if len(last) > 0 and len(last) < 46 and validator.validateStr(last):
            isValid = True
        else:
            print("Invalid name")

    isValid = False
    while isValid == False:
        secret = raw_input("Enter your password")
		if secret == compare:
            isValid = True
        else:
            print("Sorry, wrong password")

	data = (last, custID)
	if queries.updateCustomerLastName(connection, data) is None:
		print("Unable to update your name. Please try again")

def editPassword(connection, custID, compare):
	isValid = False
    while isValid == False:
        password = raw_input("\nPlease create a new password:\n")
        if validator.validatePass(password):
            isValid = True
        else:
            print("Passwords must be longer than 5 characters and contain a number")

    isValid = False
    while isValid == False:
        secret = raw_input("Enter your old password for verification")
        if secret == compare:
            isValid = True
        else:
            print("Sorry, wrong password")

	data = (password,custID) 
	if queries.updateCustomerPassword(connection, data) is None:
		print("Unable to update your password. Please try again")

def editAddress(connection, custID, compare):
	isValid = False
    while isValid == False:    
        addr = raw_input("Please enter your new address:\n")
        if len(addr) > 0 and len(addr) < 56 and validator.validateStr(addr):
            isValid = True
        else:
            print("Please enter a valid address")

    isValid = False
    while isValid == False:
        secret = raw_input("Enter your password")
        if secret == compare:
            isValid = True
        else:
            print("Sorry, wrong password")

	data = (addr,custID)
	if queries.updateCustomerAddress(connection, data) is None:
		print("Unable to update address. Please try again")
        

#Function will ask what a customer wants to edit (update in the DB) and then prompt
#that customer to add new info to update columns in tables. This function also displays a customer's current info.
def editAccount(connection, custID):
    customerInteracting = True
    while customerInteracting == True:

        #DISPLAY INFO
        print("\nYour account information (password not shown) is:")

        data = (str(custID))
		data_customer = (data,)
		customer = queries.getCustomer(connection,data_customer)
	    if customer is None:
			print("Customer not found with ID: " + data)
			return

		cards = queries.getCustomerCards(connection, data_customer)
		if cards is None:
			print("Customer credit cards could not be found with customer ID: " + data)
			return

        compare = customer[9]
        print("User ID: " + str(customer[0]))
        print("FirstName: " + customer[1])
        print("LastName: " + customer[2])
        print("Address: " + customer[3])
        print("City: " + customer[4])
        print("State: " + customer[5])
        print("Zip: " + customer[6])
        print("Phone: " + customer[7])
        print("Email: " + customer[8])
        print("\nCards:")

        for CardNumber, in cards:
            print("{}".format(CardNumber))


        #USER INPUT SECTION
        print("""\nWhat would you like to edit? Note, you cannot change your User ID. You cannot edit your credit card info. You may only delete a credit card or add a new one. Type 'back' to go back""")
        print("First Name (0)\nLast Name (1)\nPassword (2)\nAddress (3)\nCity (4)\nState (5)\nZip Code (6)\nPhone Number (7)\nEmail (8)\nDelete Card (9)\nAdd Card (10)")
        userInput = raw_input()


        #exit function
        if(userInput == "back"):
            customerInteracting = False

        # EDIT FIRST NAME   
        elif(userInput == "0"):
            editFirstName(connection, custID, compare)

        # EDIT LAST NAME   
        elif(userInput == "1"):
            editLastName(connection, custID, compare)

        # EDIT PASSWORD
        elif(userInput == "2"):
         	editPassword(connection, custID, compare)   

        # EDIT ADDRESS   
        elif(userInput == "3"):
            editAddress(connection, custID, compare)

        # EDIT CITY ######################################################
        elif(userInput == "4"):
            isValid = False
            while isValid == False:       
                city = raw_input("Please enter the city you live in now:\n")
                if len(city) > 0 and len(city) < 46:
                    isValid = True
                if "'" in city or '"' in city or ";" in city or "(" in city or ")" in city:
                    isValid = False
                if isValid == False:
                    print("Please enter a valid city")
            isValid = False
            correctPassword = False
            while isValid == False:
                secret = raw_input("Enter your password or type '1' to go back:\n")
                if secret == "1":
                    isValid = True
                elif secret == compare:
                    isValid = True
                    correctPassword = True
                else:
                    print("Sorry, wrong password")
            if correctPassword == True:
                SQL = ("UPDATE JohmpsonClothing.Customer SET City = %s WHERE CustomerID = %s;")
                data = (city,custID)
                cursor = connection.cursor()
                cursor.execute(SQL,data)
                connection.commit()
                cursor.close()
                
        # EDIT STATE ######################################################            
        elif(userInput == "5"):            
            isValid = False
            while isValid == False:    
                state = raw_input("Please enter the new state (abbreviated) you live in:\n")
		state = validator.validateState(state)
                if state is not None:
                    isValid = True
                else:
                    print("Please enter a valid state (must be abbreviated. Example: FL)")
            isValid = False
            correctPassword = False
            while isValid == False:
                secret = raw_input("Enter your password or type '1' to go back:\n")
                if secret == "1":
                    isValid = True
                elif secret == compare:
                    isValid = True
                    correctPassword = True
                else:
                    print("Sorry, wrong password")
            if correctPassword == True:
                SQL = ("UPDATE JohmpsonClothing.Customer SET State = %s WHERE CustomerID = %s;")
                data = (state,custID)
                cursor = connection.cursor()
                cursor.execute(SQL,data)
                connection.commit()
                cursor.close()
                
        # EDIT ZIP CODE ####################################################
        elif(userInput == "6"):
            isValid = False
            while isValid == False:
                zipCode = raw_input("Please enter your new zip code:\n")
                if validator.validateZip(zipCode):
                    isValid = True
                else:
                    print("Please enter a valid zip code. Format is: 'xxxxx'. 'x' is any number between 0 and 9.")
            isValid = False
            correctPassword = False
            while isValid == False:
                secret = raw_input("Enter your password or type '1' to go back:\n")
                if secret == "1":
                    isValid = True
                elif secret == compare:
                    isValid = True
                    correctPassword = True
                else:
                    print("Sorry, wrong password")
            if correctPassword == True:
                SQL = ("UPDATE JohmpsonClothing.Customer SET Zip = %s WHERE CustomerID = %s;")
                data = (zipCode,custID)
                cursor = connection.cursor()
                cursor.execute(SQL,data)
                connection.commit()
                cursor.close()
                
        # EDIT PHONE NUMBER #################################################
        elif(userInput == "7"):
            isValid = False
            while isValid == False:
                phone = raw_input("Please enter your new phone number:\n")
                if validator.validatePhone(phone):
                    isValid = True
                else:
                    print("Please enter a valid phone number. Format is: '(Xxx) Xxx-xxxx'. 'X' is any number between 1 and 9 and 'x' is any number between 0 and 9.")
            isValid = False
            correctPassword = False
            while isValid == False:
                secret = raw_input("Enter your password or type '1' to go back:\n")
                if secret == "1":
                    isValid = True
                elif secret == compare:
                    isValid = True
                    correctPassword = True
                else:
                    print("Sorry, wrong password")
            if correctPassword == True:
                SQL = ("UPDATE JohmpsonClothing.Customer SET Phone = %s WHERE CustomerID = %s;")
                data = (phone,custID)
                cursor = connection.cursor()
                cursor.execute(SQL,data)
                connection.commit()
                cursor.close()
                
        # EDIT EMAIL #########################################################
        elif(userInput == "8"):
            isValid = False
            while isValid == False:
                email = raw_input("Please enter your new email address:\n")
                if len(email) > 4 and len(email) < 256 and "@" in email and "." in email:
                    isValid = True
                if "'" in email or '"' in email or ";" in email or "(" in email or ")" in email:
                    isValid = False
                if isValid == False:
                    print("Please enter a valid email address")
            isValid = False
            correctPassword = False
            while isValid == False:
                secret = raw_input("Enter your password or type '1' to go back:\n")
                if secret == "1":
                    isValid = True
                elif secret == compare:
                    isValid = True
                    correctPassword = True
                else:
                    print("Sorry, wrong password")
            if correctPassword == True:
                SQL = ("UPDATE JohmpsonClothing.Customer SET Email = %s WHERE CustomerID = %s;")
                data = (email,custID)
                cursor = connection.cursor()
                cursor.execute(SQL,data)
                connection.commit()
                cursor.close()

        # DELETE A CREDIT CARD, WILL MAKE YOU ADD A NEW ONE IF YOU ONLY HAVE ONE CREDIT CARD
        elif(userInput == "9"):
            isValid = False
            while isValid == False:
                toDelete = raw_input("Please enter the card number of the card you wish to be deleted\n")
                if (toDelete,) in cards:
                    isValid = True
                else:
                    print("That card is incorrect")
            isValid = False
            correctPassword = False
            while isValid == False:
                secret = raw_input("Enter your password or type '1' to go back:\n")
                if secret == "1":
                    isValid = True
                elif secret == compare:
                    isValid = True
                    correctPassword = True
                else:
                    print("Sorry, wrong password")
            if correctPassword == True:
                cursor = connection.cursor()
                SQL = (" DELETE FROM JohmpsonClothing.CreditCards WHERE CardNumber = %s;")
                data = (toDelete,)
                cursor.execute(SQL,data)
                connection.commit()
                cursor.close
                print("Your credit card has been deleted")
                if len(cards) < 2:
                    print("You must now enter a new credit card")
                    cursor = connection.cursor()
                    cardInfo = createUser.addCard()
                    cardSQL = (""" insert into JohmpsonClothing.CreditCards (CardNumber, SecurityCode, Customer, ValidDate, ExpirationDate)
                                    Values (%s,%s,%s,%s,%s);""")
                    card_data = (cardInfo[0], cardInfo[1],custID, cardInfo[2], cardInfo[3])
                    cursor.execute(cardSQL,card_data)
                    connection.commit()
                    cursor.close

        # ADD A NEW CREDIT CARD ############################################################            
        elif(userInput == "10"):
            cursor = connection.cursor()
            print("")
            cardInfo = createUser.addCard()         
            isValid = False
            correctPassword = False
            while isValid == False:
                secret = raw_input("Enter your password or type '1' to go back and cancel:\n")
                if secret == "1":
                    isValid = True
                elif secret == compare:
                    isValid = True
                    correctPassword = True
                else:
                    print("Sorry, wrong password")
            if correctPassword == True:
                cardSQL = (""" insert into JohmpsonClothing.CreditCards (CardNumber, SecurityCode, Customer, ValidDate, ExpirationDate)
                                Values (%s,%s,%s,%s,%s);""")
                card_data = (cardInfo[0], cardInfo[1],custID, cardInfo[2], cardInfo[3])
                cursor.execute(cardSQL,card_data)
                connection.commit()
                cursor.close
