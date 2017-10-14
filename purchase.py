import validator
import queries
from datetime import date

# Make a purchase.
# Will ask user which store to buy an item (purchaseInput) from, quantity of item, and where they want the bill to be billed to
def purchase(connection, custID, inID, purchaseInput):

    # get neccessary info
	data_card = (custID,)
	data_purchase = (purchaseInput,)
	stores = queries.getStoresWithItem(connection, data_purchase)
	price = queries.getPriceItem(connection, data_purchase)
	realPrice = price[0]
	amount = 0
	billingAddress = ""
	billingCity = ""
	billingState = ""
	billingZip = ""
	quant = 0
	card_input = ""
	storeSelection = -1

	# If there are stores with that item in stock, continue
	if (stores is not None) and (price is not None):
		storeIds = []
		for (StoreId, Address, Inventory) in stores:
			storeIds.append(str(StoreId))
			print("{}, {}, {} ".format(StoreId, Address, Inventory))

		# SELECT STORE
		isValid = False
		while isValid == False:         
			storeSelection = raw_input("Enter the Store's ID number to select a store to buy your item from:\n")
			if storeSelection.isdigit() == True:
				if storeSelection in storeIds:
					isValid = True
				else:
					print("Incorrect input")
			else:
				print("Incorrect input")

		# GET QUANTITY
		isValid = False
		while isValid == False:
			quant = raw_input("How many of this item would you like to buy?\n")
			try:
				amount = int(quant) * realPrice
				isValid = True
			except:
				print("Incorrect Input")

		# GET BILLING ADDRESS LINE
		isValid = False
		while isValid == False:    
			billingAddress = raw_input("Please enter the billing address:\n")
			if len(billingAddress) > 0 and len(billingAddress) < 56 and validator.validateStr(billingAddress):
				isValid = True
			else:
				print("Please enter a valid address")

		# GET BILLING CITY
		isValid = False
		while isValid == False:       
			billingCity = raw_input("Please enter the city that this purchase will be billed to:\n")
			if len(billingCity) > 0 and len(billingCity) < 46 and validator.validateStr(billingCity):
				isValid = True
			else:
				print("Please enter a valid city")
        
		# GET BILLING STATE        
		isValid = False
		while isValid == False:    
			billingState = raw_input("Please enter the state (abbreviated) that this purchase will be billed to:\n")
			billingState = validator.validateState(billingState)
			if billingState is not None:
				isValid = True
			else:
				print("Please enter a valid state (must be abbreviated. Example: FL)")

		# GET BILLING ZIP
		isValid = False
		while isValid == False:
			billingZip = raw_input("And finally the zip code:\n")
			if validator.validateZip(billingZip):
				isValid = True
			else:
				print("Please enter a valid zip code. Format is: 'xxxxx'. 'x' is any number between 0 and 9.")       

		# SELECT CARD TO USE
		print("Credit Cards")
		creditCards = queries.getCustomerCards(connection, data_card)
		if creditCards is None:
			print("You do not have any credit cards on file. Please add one")
			return 
		i = 0
		print("{0:6}{1:32}".format("Row", "Card Number"))
		for (CardNumber,) in creditCards:
			print("{0:6}{1:32}".format(str(i),CardNumber))
			i = i + 1
				
		isValid = False
		while isValid == False:
			card_input = raw_input("Please select which credit card to use by inputing your cardnumber:\n")
			if (card_input,) in creditCards:
				isValid = True
			else:
				print("Incorrect card number")              
        
        # GET A FINAL CONFIRMATION AND EXECUTE
		confirmation = raw_input("Are you sure you would like to make this purchase? (y/n)\n")
		if confirmation == "y":
			yearMonthDay = date.today()
			data_invoice = (custID, billingAddress, billingCity, billingState, billingZip, yearMonthDay)
			data_quantity = (purchaseInput, storeSelection)
			lineInfo = [purchaseInput, quant, amount, card_input]
			invoiceID = queries.placeOrder(connection, data_quantity, data_invoice, lineInfo)
			if invoiceID is not None:
				print("Your order has been placed. Your invoice ID is: " + str(invoiceID))
			else:
				print("Could not place order")
		else:
			print("Very well. Your order has been cancelled")
	else:
		print("Sorry, that item is not in stock at any of our stores")
