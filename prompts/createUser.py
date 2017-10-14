from passlib.hash import pbkdf2_sha256
import utils.validator as validator
import utils.queries as queries
import card

#Registers a new customer. Also a bunch of prompts for user input. Inserts into the customer table and credit card table            
def customerRegistration(connection):
    isValid = False
    # CREATE PASSWORD
    while isValid == False:
		password = raw_input("\nPlease create a password:\n")
		if validator.validatePass(password):
			password = pbkdf2_sha256.hash(password)
			isValid = True
		else:
			print("Passwords must be longer than 5 characters and contain a number")

    # CREATE FIRST NAME       
    isValid = False
    while isValid == False:      
        first = raw_input("Please enter your first name:\n")
        if len(first) > 0 and len(first) < 46 and validator.validateStr(first):
            isValid = True
        else:
            print("Invalid Name")

    # CREATE LAST NAME
    isValid = False
    while isValid == False:     
        last = raw_input("Please enter your last name:\n")
        if len(last) > 0 and len(last) < 46 and validator.validateStr(last):
            isValid = True
	else:
            print("Invalid name")

    # CREATE ADDRESS
    isValid = False
    while isValid == False:    
        addr = raw_input("Please enter your address:\n")
        if len(addr) > 0 and len(addr) < 56 and validator.validateStr(addr):
            isValid = True
	else:
            print("Please enter a valid address")

    # CREATE CITY
    isValid = False
    while isValid == False:       
        city = raw_input("Please enter the city you live in:\n")
        if len(city) > 0 and len(city) < 46:
            isValid = True
        if "'" in city or '"' in city or ";" in city or "(" in city or ")" in city:
            isValid = False
        if isValid == False:
            print("Please enter a valid city")

    # CREATE STATE       
    isValid = False
    while isValid == False:    
        state = raw_input("Please enter the state (abbreviated) you live in:\n")
	state = validator.validateState(state)
        if state is not None:
            isValid = True
        else:
            print("Please enter a valid state (must be abbreviated. Example: FL)")

    # CREATE ZIP CODE
    isValid = False
    while isValid == False:
        zipCode = raw_input("Please enter your zip code:\n")
        if validator.validateZip(zipCode):
            isValid = True
        else:
            print("Please enter a valid zip code. Format is: 'xxxxx'. 'x' is any number between 0 and 9.")

    # CREATE PHONE NUMBER
    isValid = False
    while isValid == False:
        phone = raw_input("Please enter your phone number:\n")
        if validator.validatePhone(phone):
            isValid = True
        else:
            print("Please enter a valid phone number. Format is: '(Xxx) Xxx-xxxx'. 'X' is any number between 1 and 9 and 'x' is any number between 0 and 9.")

    # CREATE EMAIL
    isValid = False
    while isValid == False:
        email = raw_input("Please enter your email address:\n")
        if validator.validateEmail(email) and validator.validateStr(email):
            isValid = True
        else:
            print("Please enter a valid email address")

    # CREATE CREDIT CARD (CALLS ADD CARD)
    cardInfo = card.addCard()

    # ASSEMBLES DATA AND INSERTS IT INTO THE CUSTOMER TABLE AND CREDIT CARDS TABLE        
    data_customer = (password,last,first,addr,city,state,zipCode,phone,email)
    print("Are you sure you would like to make an account? (y)")
    confirmation = raw_input()
    if confirmation == "y":
	myId = queries.insertCustomer(connection, data_customer, cardInfo)
	if myId is not None:
		print("Your account has been created! YOUR USER ID IS: " + str(myId))
	else:
		print("Your account has not been created")
        
    else:
        print("Your account has not been created")
