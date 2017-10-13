import validator

#This function does not add a card in the database. It is a series of prompts that collects valid credit card info and puts it in a list called array
#This function returns the array if everything is valid. It will always return an array bcause it will only accept valid info
###########################################################################################################################
def addCard():
    isValid = False
    while isValid == False:
        cardNumber = raw_input("Please enter your Credit Card Number (5522890707555845 is an example):\n")
        if validator.validateCreditCard(cardNumber):
            isValid = True
        else:
            print("Please enter a valid credit card number")

    isValid = False
    while isValid == False:
        cardSecurity = raw_input("Please enter the security code on the back of your card:\n")
        if validator.validateSecurityCode(cardSecurity):
            isValid = True
        else:
            print("Please enter a valid security code")

    isValid = False
    while isValid == False:
        endDate = raw_input("Please enter when your card expires (mm-yyyy):\n")
        if validator.validateEndDate(endDate) is not None:
            isValid = True
        else:
            print("Incorrect Date Format")
    array = [cardNumber, cardSecurity, endDate]
    return array

#Registers a new customer. Also a bunch of prompts for user input. Inserts into the customer table and credit card table         
###########################################################################################################################    
def customerRegistration(connection):
    isValid = False
    SQL = ("""  Insert into JohmpsonClothing.Customer (Password, LastName, FirstName, Address, City, State, Zip, Phone, Email)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);""")
    cardSQL = (""" insert into JohmpsonClothing.CreditCards (CardNumber, SecurityCode, Customer, ValidDate, ExpirationDate)
                Values (%s,%s,%s,%s,%s);""")

    # CREATE PASSWORD #################################
    while isValid == False:
        password = raw_input("\nPlease create a password:\n")
        if validator.validatePass(password):
            isValid = True
        else:
            print("Passwords must be longer than 5 characters and contain a number")

    # CREATE FIRST NAME ###############################       
    isValid = False
    while isValid == False:      
        first = raw_input("Please enter your first name:\n")
        if len(first) > 0 and len(first) < 46:
            isValid = True
        if "'" in first or '"' in first or ";" in first or "(" in first or ")" in first:
            isValid = False
        if isValid == False:
            print("Invalid name")

    # CREATE LAST NAME #################################
    isValid = False
    while isValid == False:     
        last = raw_input("Please enter your last name:\n")
        if len(last) > 0 and len(last) < 46:
            isValid = True
        if "'" in last or '"' in last or ";" in last or "(" in last or ")" in last:
            isValid = False
        if isValid == False:
            print("Invalid name")

    # CREATE ADDRESS ####################################
    isValid = False
    while isValid == False:    
        addr = raw_input("Please enter your address:\n")
        if len(addr) > 0 and len(addr) < 56:
            isValid = True
        if "'" in addr or '"' in addr or ";" in addr or "(" in addr or ")" in addr:
            isValid = False
        if isValid == False:
            print("Please enter a valid address")

    # CREATE CITY #######################################
    isValid = False
    while isValid == False:       
        city = raw_input("Please enter the city you live in:\n")
        if len(city) > 0 and len(city) < 46:
            isValid = True
        if "'" in city or '"' in city or ";" in city or "(" in city or ")" in city:
            isValid = False
        if isValid == False:
            print("Please enter a valid city")

    # CREATE STATE ######################################        
    isValid = False
    while isValid == False:    
        state = raw_input("Please enter the state (abbreviated) you live in:\n")
	state = validator.validateState(state)
        if state is not None:
            isValid = True
        else:
            print("Please enter a valid state (must be abbreviated. Example: FL)")

    # CREATE ZIP CODE ####################################
    isValid = False
    while isValid == False:
        zipCode = raw_input("Please enter your zip code:\n")
        if validator.validateZip(zipCode):
            isValid = True
        else:
            print("Please enter a valid zip code. Format is: 'xxxxx'. 'x' is any number between 0 and 9.")

    # CREATE PHONE NUMBER ################################
    isValid = False
    while isValid == False:
        phone = raw_input("Please enter your phone number:\n")
        if validator.validatePhone(phone):
            isValid = True
        else:
            print("Please enter a valid phne number. Format is: '(Xxx) Xxx-xxxx'. 'X' is any number between 1 and 9 and 'x' is any number between 0 and 9.")

    # CREATE EMAIL ########################################
    isValid = False
    while isValid == False:
        email = raw_input("Please enter your email address:\n")
        if len(email) > 4 and len(email) < 256 and "@" in email and "." in email:
            isValid = True
        if "'" in email or '"' in email or ";" in email or "(" in email or ")" in email:
            isValid = False
        if isValid == False:
            print("Please enter a valid email address")

    # CREATE CREDIT CARD (CALLS ADD CARD) #################
    cardInfo = addCard()

    # ASSEMBLES DATA AND INSERTS IT INTO THE CUSTOMER TABLE AND CREDIT CARDS TABLE        
    data_customer = (password,last,first,addr,city,state,zipCode,phone,email)
    print("Are you sure you would like to make an account? (y)")
    confirmation = raw_input()
    if confirmation == "y":
        cursor = connection.cursor()
        cursor.execute(SQL,data_customer)
        connection.commit()
        cursor.execute("""  select max(CustomerID)
                            from Customer;""")
        maxID = cursor.fetchone()
        data_card = (cardInfo[0], cardInfo[1], maxID[0], cardInfo[2])
        cursor.execute(cardSQL,data_card)
        connection.commit()
        cursor.close()
        print("Your account has been created! YOUR USER ID IS: " + str(maxID[0]))
        
    else:
        print("Your account has not been created")
