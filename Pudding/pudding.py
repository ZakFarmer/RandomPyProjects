from cosby import BillCosby

bill = BillCosby(1000, True)

bill.x = 15

print("Bill Cosby is", bill.age, "years old.")
print("His hobbies are", bill.hobbies[0].lower(), "and", bill.hobbies[1].lower())
