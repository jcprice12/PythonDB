import purchase
import queries

#Function that will take user input on how to order our clothing articles (for print-out)
#After it calls orderBy, this function will call purchase if input is valid. Input will be the clothing ID of the article of clothing you want to buy
def viewAndPlace(connection, custID, inID):
    customerInteracting = True                     
    while customerInteracting == True:
        user_input = raw_input("Order by: ID No (0), Name (1), Type (2), Season (3), Price (4), Material (5)\n")
		myDict={
			"0":"ClothingID",
			"1":"Name",
			"2":"Type",
			"3":"Season",
			"4":"Price",
			"5":"Material"
		}
		val = myDict.get(user_input,"back")
		if val == "back":
			return
		else:
			if not queries.printClothesInOrder(connection,val):
				return

        isValid = False
        while isValid == False:     
            user_input = raw_input("\nTo purchase an item, input its ID No. Type 'back' to go back to your action screen\n")
	    	if user_input == "back":
        		return

            try:
            	user_inp = int(user_input2)
            	isValid = True
            except:
                print("That's an invalid id")

		article = queries.selectArticle(user_input)
        if article == None:
            print("That clothing item doesn't exist")
        else:
            purchase.purchase(connection, custID, inID, article[0])


