import utils.validator as validator

#This function does not add a card in the database. It is a series of prompts that collects valid credit card info and puts it in a list called array
#This function returns the array if everything is valid. It will always return an array bcause it will only accept valid info
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
