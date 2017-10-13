from datetime import datetime
import re

def validateStr(s):
	badChars = set('\"\';()*+-/{}[]')
	if not any((c in badChars) for c in s):
		return True
	else:
		return False

def validateEndDate(endDate):
	match = re.search('^((0[1-9]|1[0-2])-2[0-9][0-9][0-9])$', endDate)
	if match:
		endDate += '-01'
		print(endDate)
		try:
			datetime_obj = datetime.strptime(endDate, '%m-%Y-%d')
			return datetime_obj
	    	except:
			return None
	else:
		return None

def validatePhone(phone):
	match = re.search('^(\([1-9][0-9][0-9]\) [1-9][0-9][0-9]-[0-9][0-9][0-9][0-9])$', phone)
	if match:
		return True
	else:
		return False

def validateEmail(email):
	if len(email) < 256:
		match = re.search('[^@]+@[^@]+\.[^@]+', email)
		if match:
			return True
		else:
			return False
	else:
		return False

def validateSecurityCode(code):
	if len(code) == 3:
		match = re.search('^([0-9][0-9][0-9])$', code)
		if match:
			return True
		else:
			return False
	else:
		return False

def validateCreditCard(cardNo):
	cardNo.replace("-","")
	length = len(cardNo)
	if (length == 16) and (cardNo.isdigit()):
		last = cardNo[length-1]
	    	temp = cardNo[::-1]
	    	string = ""
	    	count = 0
	    	for x in range(1,length):
			if count % 2 == 0:
		    		i = int(temp[x])
		    		i = i * 2
		    		if i > 9:
					i = i - 9
		    		string = string + str(i)
			else:
		    		string = string + temp[x]
			count = count + 1
	    	total = 0
	    	for x in range(0,length-1):
			i = int(string[x])
			total = total + i
	    	if (total % 10) != int(last):
			return False
	    	return True
	else:
		return False

def validateState(state):
	states = ("AK","AL","AR","AZ","CA","CO","CT","DE","FL","GA","HI","IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND","NE","NH","NJ","NM","NV","NY",
              "OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VA","VT","WA","WI","WV","WY")

	if len(state) == 2:
		state = state.upper()
		first = 0
		last = 49
		found = False
		while first <= last and not found:
			middle = ((last + first) // 2)
			currentState = states[middle]
			if currentState == state:
				found = True
			elif state < currentState:
				last = middle - 1
			else:
				first = middle + 1
		if found:
			return state
		else:
			return None
	else:
		return None

def validateZip(myZip):
	if len(myZip) == 5 and myZip.isdigit():
		return True
	else:
		return False

def validatePass(password):
	if len(password) > 5 and len(password) < 56:
		myNumbers = set('0123456789')
		badChars = set('\"\';()*+-/{}[]')
		if validateStr(password) and (any((c in myNumbers) for c in password)):
			return True
		else:
			return False
	else:
		return False


print(validatePass("1234567"))








