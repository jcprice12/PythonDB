from mysql.connector import errorcode
import createUser

def printClothesInOrder(connection, order):
	cursor = connection.cursor()
	try:
		data = (order)
	    	cursor.execute("""  select *
		                from Clothing
		                order by %s;""", data)
	    	clothing = cursor.fetchall()
	    	cursor.close()
	    	print("{0:15}{1:20}{2:20}{3:8}{4:10}{5:15}".format("Clothing ID", "Name", "Type", "Season", "Price", "Material"))
	    	for (ClothingID, Name, Type, Season, Price, Material) in clothing:
	    		print("{0:15}{1:20}{2:20}{3:8}${4:10}{5:15}".format(str(ClothingID), Name, Type, Season, str(Price), Material))
		return True
	except:
		print("Error occurred printing clothes")
		return False

def selectArticle(connection,articleId):
	cursor = connection.cursor()
	try:
		SQL = ("  SELECT ClothingID "
		            "FROM Clothing "
		            "WHERE ClothingID = %s;")
		data = (articleId)
		cursor.execute(SQL,data)
		article = cursor.fetchone()
		cursor.close()
		return article
	except:
		print("Error occurred retrieving article")
		return None

def insertCustomer(connection, data_customer, cardInfo):
	SQL = ("""  Insert into JohmpsonClothing.Customer (Password, LastName, FirstName, Address, City, State, Zip, Phone, Email)
        		VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);""")
	cardSQL = (""" insert into JohmpsonClothing.CreditCards (CardNumber, SecurityCode, Customer, ValidDate, ExpirationDate)
        		Values (%s,%s,%s,%s,%s);""")
	
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
                        	where ClothingID = %s and Inventory > 0;
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
                        	where ClothingID = %s;""")
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
		            where CustomerID = %s;""")
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
		                where Customer = """ + str(custID) + """;""")
		cursor.execute(SQL, data_customer)
		cards = cursor.fetchall()
		cursor.close()
		return cards
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		cursor.close()
		return None

def updateCustomerFirstName(connection, data):
	cursor = connection.cursor()
	SQL = ("UPDATE JohmpsonClothing.Customer SET FirstName = %s WHERE CustomerID = %s;")
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
	SQL = ("UPDATE JohmpsonClothing.Customer SET LastName = %s WHERE CustomerID = %s;")
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
	SQL = ("UPDATE JohmpsonClothing.Customer SET Password = %s WHERE CustomerID = %s;")
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
	SQL = ("UPDATE JohmpsonClothing.Customer SET Address = %s WHERE CustomerID = %s;")
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
	SQL = ("UPDATE JohmpsonClothing.Customer SET City = %s WHERE CustomerID = %s;")
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
	SQL = ("UPDATE JohmpsonClothing.Customer SET State = %s WHERE CustomerID = %s;")
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
	SQL = ("UPDATE JohmpsonClothing.Customer SET Zip = %s WHERE CustomerID = %s;")
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
	SQL = ("UPDATE JohmpsonClothing.Customer SET Phone = %s WHERE CustomerID = %s;")
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
	SQL = ("UPDATE JohmpsonClothing.Customer SET Email = %s WHERE CustomerID = %s;")
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
        SQL = (" DELETE FROM JohmpsonClothing.CreditCards WHERE CardNumber = %s;")

	try:
        	cursor.execute(SQL,data)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None

	if len(cards) < 2:
		cardSQL = (""" insert into JohmpsonClothing.CreditCards (CardNumber, SecurityCode, Customer, ValidDate, ExpirationDate)
                        Values (%s,%s,%s,%s,%s);""")
		print("You must now enter a new credit card")
		cardInfo = createUser.addCard()
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
                        Values (%s,%s,%s,%s,%s);""")
	try:
        	ursor.execute(cardSQL,data)
	except mysql.connector.Error as err:
		print("Something went wrong: {}".format(err))
		connection.rollback()
		cursor.close()
		return None

        connection.commit()
        cursor.close()
	return True

		
		






