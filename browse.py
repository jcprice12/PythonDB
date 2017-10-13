import purchase

#Function that prints out all of our clothing options, ordered by user input (order)
###########################################################################################################################
def orderBy(order, connection):
    cursor = connection.cursor()
    cursor.execute("""  select *
                        from Clothing
                        order by """ + order + """;""")
    clothing = cursor.fetchall()
    cursor.close()
    print("{0:15}{1:20}{2:20}{3:8}{4:10}{5:15}".format("Clothing ID", "Name", "Type", "Season", "Price", "Material"))
    for (ClothingID, Name, Type, Season, Price, Material) in clothing:
        print("{0:15}{1:20}{2:20}{3:8}${4:10}{5:15}".format(str(ClothingID), Name, Type, Season, str(Price), Material))

#Function that will take user input on how to order our clothing articles (for print-out)
#After it calls orderBy, this function will call purchase if input is valid. Input will be the clothing ID of the article of clothing you want to buy
###########################################################################################################################
def viewAndPlace(connection, custID, inID):
    customerInteracting = True                     
    while customerInteracting == True:
        user_input = raw_input("Order by: ID No (0), Name (1), Type (2), Season (3), Price (4), Material (5)\nType 'back to go back\n")
        if user_input == "back":
            return
        elif user_input == "0":
            orderBy("ClothingID",connection)
        elif user_input == "1":
            orderBy("Name",connection)
        elif user_input == "2":
            orderBy("Type",connection)
        elif user_input == "3":
            orderBy("Season",connection)
        elif user_input == "4":
            orderBy("Price",connection)
        elif user_input == "5":
            orderBy("Material",connection)
        isValid = False
        while isValid == False:     
            user_input2 = raw_input("\nTo purchase an item, input its ID No. Type 'back' to go back to your action screen\n")
            try:
                if user_input2 == "back":
                    isValid = True
                else:
                    user_inp = int(user_input2)
                    isValid = True
            except:
                print("That's an invalid id")
        if user_input2 == "back":
            customerInteracting = False
        else:
            cursor = connection.cursor()
            SQL = ("  SELECT ClothingID "
                        "FROM Clothing "
                        "WHERE ClothingID = %s;")
            data = (user_input2,)
            cursor.execute(SQL,data)
            article = cursor.fetchone()
            cursor.close()
            if article == None:
                print("That clothing item doesn't exist")
            else:
                isValid = True
                purchase.purchase(connection, custID, inID, article[0])
