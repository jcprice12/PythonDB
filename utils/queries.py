import mysql.connector
from mysql.connector import errorcode
import prompts.card as card

def printClothesInOrder(connection, order):
	cursor = connection.cursor()
	try:
		data = (order,)
	    	cursor.execute("""  select *
		                from Clothing
		                order by %s""", data)
	    	clothing = cursor.fetchall()
	    	cursor.close()
	    	print("{0:15}{1:20}{2:20}{3:8}{4:10}{5:15}".format("Clothing ID", "Name", "Type", "Season", "Price", "Material"))
	    	for (ClothingID, Name, Type, Season, Price, Material) in clothing:
	    		print("{0:15}{1:20}{2:20}{3:8}${4:10}{5:15}".format(str(ClothingID), Name, Type, Season, str(Price), Material))
		return True
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		cursor.close()
		return False

def printOrders(connection, data):
	cursor = connection.cursor()
	try:
		SQL = """select InvoiceID, InvoiceLineID, ClothingID, Name, SoldFor, Credit
                         from (JohmpsonClothing.Clothing natural join JohmpsonClothing.InvoiceLine) natural join JohmpsonClothing.Invoice
                         where CustomerID = %s"""
		cursor.execute(SQL, data)
		print("{0:11}{1:10}{2:12}{3:20}{4:10}{5:32}".format("Invoice ID", "Line ID", "Clothing ID", "Name", "Sold For", "Credit Card"))
            	for (InvoiceID, InvoiceLineId, ClothingId, Name, SoldFor, Credit) in cursor:
                	print("{0:11}{1:10}{2:12}{3:20}${4:9}{5:32}".format(str(InvoiceID), str(InvoiceLineId), str(ClothingId), Name, str(SoldFor), Credit))
		cursor.close()
		return True
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		cursor.close()
		return False

def selectArticle(connection,articleId):
	cursor = connection.cursor()
	try:
		SQL = (""" SELECT ClothingID 
		             FROM Clothing 
		             WHERE ClothingID = %s""")
		data = (articleId,)
		cursor.execute(SQL, data)
		article = cursor.fetchone()
		cursor.close()
		return article
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		cursor.close()
		return None

def insertCustomer(connection, data_customer, cardInfo):
	SQL = ("""  Insert into JohmpsonClothing.Customer (Password, LastName, FirstName, Address, City, State, Zip, Phone, Email)
        		VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""")
	cardSQL = (""" insert into JohmpsonClothing.CreditCards (CardNumber, SecurityCode, Customer, ExpirationDate)
        		Values (%s,%s,%s,%s)""")
	
	cursor = connection.cursor()
	try:	
		cursor.execute(SQL,data_customer)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None

	myId = cursor.lastrowid

	data_card = (cardInfo[0], cardInfo[1], myId, cardInfo[2])
	try:
		cursor.execute(cardSQL,data_card)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None

	connection.commit()
	cursor.close()
	return myId

def getStoresWithItem(connection, data_purchase):
	cursor = connection.cursor()
	try:
		storesSQL = ("""select StoreId, Address, Inventory
                		from JohmpsonClothing.StoresClothing natural join JohmpsonClothing.Stores
                        	where ClothingID = %s and Inventory > 0
				order by StoreId asc""")
		cursor.execute(storesSQL,data_purchase)
		stores = cursor.fetchall()
		cursor.close()
		return stores
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		cursor.close()
		return None

def getPriceItem(connection, data_purchase):
	cursor = connection.cursor()
	try:
		priceSQL = (""" select Price
                        	from JohmpsonClothing.Clothing
                        	where ClothingID = %s""")
		cursor.execute(priceSQL, data_purchase)
		price = cursor.fetchone()
		cursor.close()
		return price
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		cursor.close()
		return None

def getCustomer(connection, data_customer):
	cursor = connection.cursor()
	try:
		SQL = ("""  select CustomerID, FirstName, LastName, Address, City, State, Zip, Phone, Email, Password
		            from JohmpsonClothing.Customer
		            where CustomerID = %s""")
		cursor.execute(SQL, data_customer)
		customer = cursor.fetchone()
		cursor.close()
		return customer
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		cursor.close()
		return None

def getCustomerCards(connection, data_customer):
	cursor = connection.cursor()
	try:
		cardSQL = ("""  select CardNumber
		                from JohmpsonClothing.CreditCards
		                where Customer = %s""")
		cursor.execute(cardSQL, data_customer)
		cards = cursor.fetchall()
		cursor.close()
		return cards
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		cursor.close()
		return None

def updateCustomerFirstName(connection, data):
	cursor = connection.cursor()
	SQL = ("UPDATE JohmpsonClothing.Customer SET FirstName = %s WHERE CustomerID = %s")
	try:
		cursor.execute(SQL, data)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None
	
	connection.commit()
	cursor.close()
	return True

def updateCustomerLastName(connection, data):
	SQL = ("UPDATE JohmpsonClothing.Customer SET LastName = %s WHERE CustomerID = %s")
	cursor = connection.cursor()
	try:
		cursor.execute(SQL,data)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None

	connection.commit()
	cursor.close()
	return True

def updateCustomerPassword(connection, data):
	SQL = ("UPDATE JohmpsonClothing.Customer SET Password = %s WHERE CustomerID = %s")
        cursor = connection.cursor()
	try:
        	cursor.execute(SQL,data)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None

        connection.commit()
        cursor.close()
	return True

def updateCustomerAddress(connection, data):
	SQL = ("UPDATE JohmpsonClothing.Customer SET Address = %s WHERE CustomerID = %s")
        cursor = connection.cursor()
	try:
        	cursor.execute(SQL,data)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None

        connection.commit()
        cursor.close()
	return True

def updateCustomerCity(connection, data):
	SQL = ("UPDATE JohmpsonClothing.Customer SET City = %s WHERE CustomerID = %s")
	cursor = connection.cursor()
	try:
		cursor.execute(SQL,data)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None
	
	connection.commit()
	cursor.close()
	return True

def updateCustomerState(connection, data):
	SQL = ("UPDATE JohmpsonClothing.Customer SET State = %s WHERE CustomerID = %s")
        cursor = connection.cursor()
	try:
        	cursor.execute(SQL,data)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None

        connection.commit()
        cursor.close()
	return True

def updateCustomerZip(connection, data):
	SQL = ("UPDATE JohmpsonClothing.Customer SET Zip = %s WHERE CustomerID = %s")
        cursor = connection.cursor()
	try:
        	cursor.execute(SQL,data)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None

        connection.commit()
        cursor.close()
	return True

def updateCustomerPhone(connection, data):
	SQL = ("UPDATE JohmpsonClothing.Customer SET Phone = %s WHERE CustomerID = %s")
        cursor = connection.cursor()
	try:
        	cursor.execute(SQL,data)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None

        connection.commit()
        cursor.close()
	return True

def updateCustomerEmail(connection, data):
	SQL = ("UPDATE JohmpsonClothing.Customer SET Email = %s WHERE CustomerID = %s")
        cursor = connection.cursor()
	try:
        	cursor.execute(SQL,data)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None

        connection.commit()
        cursor.close()
	return True

def deleteAndAddCustomerCard(connection, data, cards):
	cursor = connection.cursor()
        SQL = (" DELETE FROM JohmpsonClothing.CreditCards WHERE CardNumber = %s")

	try:
        	cursor.execute(SQL,data)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None

	if len(cards) < 2:
		cardSQL = (""" insert into JohmpsonClothing.CreditCards (CardNumber, SecurityCode, Customer, ValidDate, ExpirationDate)
                        Values (%s,%s,%s,%s,%s)""")
		print("You must now enter a new credit card")
		cardInfo = card.addCard()
		card_data = (cardInfo[0], cardInfo[1],custID, cardInfo[2], cardInfo[3])
		try:
			cursor.execute(cardSQL,card_data)
		except mysql.connector.Error as err:
			print("Something went wrong: {}".format(err))
			connection.rollback()
			cursor.close()
			return None
		connection.commit()
        	cursor.close()
		return True
	else:
		connection.commit()
		cursor.close()
		return True

def addCustomerCard(connection, data):
	cursor = connection.cursor()
	cardSQL = (""" insert into JohmpsonClothing.CreditCards (CardNumber, SecurityCode, Customer, ValidDate, ExpirationDate)
                        Values (%s,%s,%s,%s,%s)""")
	try:
        	cursor.execute(cardSQL,data)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None

        connection.commit()
        cursor.close()
	return True

def placeOrder(connection, data_quantity, data_invoice, lineInfo):
	cursor = connection.cursor()
	determineQuantitySQL = (""" select Inventory 
					from StoresClothing 
					where ClothingID = %s and StoreID = %s""")
	invoiceSQL = (""" insert into JohmpsonClothing.Invoice (CustomerID, BillingAddress, BillingCity, BillingState, BillingZip, DateOfInvoice)
				values (%s,%s,%s,%s,%s,%s)""")
	invoiceLineSQL = ("""insert into JohmpsonClothing.InvoiceLine (InvoiceID, ClothingID, Quantity, SoldFor, Credit)
				values (%s,%s,%s,%s,%s)""")
	reduceInventorySQL = ("""update StoresClothing set Inventory = (Inventory - %s) where ClothingID = %s and StoreID = %s""")

	inventory = 0
	try:
		cursor.execute(determineQuantitySQL, data_quantity)
		inventory = cursor.fetchone()
		inventory = inventory[0]
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None

	if inventory < lineInfo[1]:
		print("There is not enough inventory in the store to place this order")
		return None

	
	try:
		cursor.execute(reduceInventorySQL, (lineInfo[1], data_quantity[0], data_quantity[1]))
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None	

	try:
		cursor.execute(invoiceSQL, data_invoice)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None

	invoiceId = cursor.lastrowid
	data_line = (invoiceId, lineInfo[0], lineInfo[1], lineInfo[2], lineInfo[3])

	try:
		cursor.execute(invoiceLineSQL, data_line)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None

	connection.commit()
        cursor.close()
	return invoiceId



