from mysql.connector import errorcode

def printClothesInOrder(connection, order):
	try:
		cursor = connection.cursor()
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
	try:
		cursor = connection.cursor()
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
