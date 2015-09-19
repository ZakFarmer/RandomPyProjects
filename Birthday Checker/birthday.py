from datetime import datetime

def birthdayCheck():
	dateNow = datetime.now()
	
	day = int(input("Day: "))
	month = int(input("Month (Number): "))
	year = int(input("Year: "))
	
	age = datetime(year, month, day, 0, 0)
	difference = datetime.now() - age
	
	days = difference.total_seconds() / 60 / 60 / 24
	years = days / 365.2425
	
	if (years >= 18):
		return True
	else:
		return False

if (birthdayCheck() == True):
	print("You can enter this website!")
else:
	print("You must be 18 or over to enter this website!")
