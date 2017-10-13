import validator
import queries
	

# Make a purchase.
# Will ask user which store to buy an item (purchaseInput) from, quantity of item, and where they want the bill to be billed to
###########################################################################################################################
def purchase(connection, custID, inID, purchaseInput):

    # get neccessary info
    cursor = connection.cursor()
    cardSQL = ("""      select CardNumber
                        from CreditCards
                        where Customer = %s;""")

    data_card = (custID,)
    data_purchase = (purchaseInput,)
	stores = queries.getStoresWithItem(connection, data_purchase)
	price = queries.getPriceItem(connection, data_purchase)
	realPrice = price[0]

    # If there are stores with that item in stock, continue
    if (stores is not None) and (price is not None):
        for (StoreId, Address, Inventory) in stores:
            print("{}, {}, {} ".format(StoreId, Address, Inventory))

        # SELECT STORE
        isValid = False
        while isValid == False:         
            storeSelection = raw_input("Enter the Store's ID number to select a store to buy your item from:\n")
            if storeSelection.isdigit() == True:
                if int(storeSelection) > 0 and int(storeSelection) < (len(stores)+1):
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

        # GET BILLING INFO
        isValid = False
        while isValid == False:    
            billingAddress = raw_input("Please enter the billing address:\n")
            if len(billingAddress) > 0 and len(billingAddress) < 56:
                isValid = True
            else:
                print("Please enter a valid address")

        isValid = False
        while isValid == False:       
            billingCity = raw_input("Please enter the city this purchase will be billed to:\n")
            if len(billingCity) > 0 and len(billingCity) < 46:
                isValid = True
            else:
                print("Please enter a valid city")
                
        isValid = False
        while isValid == False:    
            billingState = raw_input("Please enter the state (abbreviated) this purchase will be billed to:\n")
	    billingState = validator.validateState(billingState)
            if billingState is not None:
                isValid = True
            else:
                print("Please enter a valid state (must be abbreviated. Example: FL)")

        isValid = False
        while isValid == False:
            billingZip = raw_input("And finally the zip code:\n")
            if validator.validateZip(billingZip):
                isValid = True
            else:
                print("Please enter a valid zip code. Format is: 'xxxxx'. 'x' is any number between 0 and 9.")       
        # END GET BILLING INFO ###################################################################################################

        print("Credit Cards")
        cursor = connection.cursor()
        cursor.execute(cardSQL,data_card)
        creditCards = cursor.fetchall()
        cursor.close()
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
        
        # GET A FINAL CONFIRMATION AND EXECUTE #########################################################################
        confirmation = raw_input("Are you sure you would like to make this purchase? (y/n)\n")
        if confirmation == "y":
            cursor = connection.cursor()
            cursor.execute("""  select max(InvoiceID)
                                from Invoice;""")
            maxID = cursor.fetchone()# GET LATEST INVOICE ID
            cursor.close()
            invoiceLineSQL = (  "INSERT INTO JohmpsonClothing.InvoiceLine "
                                "(InvoiceID, ClothingID, Quantity, SoldFor, Credit) "
                                "VALUES (%s, %s, %s, %s, %s);")
            inventorySQL = (    "UPDATE JohmpsonClothing.StoresClothing SET Inventory = Inventory - %s "
                                "WHERE StoreID = %s and ClothingID = %s;")
            data_invoiceLine = (inID, purchaseInput, quant, amount, card_input)
            data_inventory = (quant,storeSelection,purchaseInput)
            # IF THIS IS THE FIRST PURCHASE MADE WITH THIS INVOICE ID
            if maxID[0] < inID:
                yearMonthDay = date.today()
                cursor = connection.cursor()
                invoiceSQL = (  "INSERT INTO JohmpsonClothing.Invoice "
                                "(InvoiceID, CustomerID, Total, BillingAddress, BillingCity, BillingState, BillingZip, DateOfInvoice) "
                                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s);")
                data_invoice = (inID, custID, amount, billingAddress, billingCity, billingState, billingZip, yearMonthDay)
                cursor.execute(invoiceSQL,data_invoice)
                cursor.execute(invoiceLineSQL, data_invoiceLine)
                cursor.execute(inventorySQL, data_inventory)
                connection.commit()
                print("Your order has been successfully placed")
                cursor.close()
            # IF YOU'VE MADE A PURCHASE WITH THIS INVOICE ID BEFORE
            else:
                yearMonthDay = date.today()
                cursor = connection.cursor()
                invoiceUpdateSQL = (    "UPDATE JohmpsonClothing.Invoice SET Total = Total + %s, DateOfInvoice = %s "
                                        "WHERE InvoiceID = %s;")
                data_updateInvoice = (amount,yearMonthDay,inID)
                cursor.execute(invoiceUpdateSQL, data_updateInvoice)
                cursor.execute(invoiceLineSQL, data_invoiceLine)
                cursor.execute(inventorySQL, data_inventory)
                connection.commit()
                print("Your order has been successfully placed")
                cursor.close()
        else:
            print("Very well. Your order has been cancelled")
    else:
        print("Sorry, that item is not in stock at any of our stores")
