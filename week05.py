def savings(income, fast, month1, month2, month3, month4, month5, month6):
  return income*0.9-fast-month1-month2-month3-month4-month5-month6
  

moneyEarned = float(input("Enter how much money you earned: "))
fastOffering = float(input("Enter how much you would like to pay for fast offerings: "))

item1 = input("Enter Item 1: ") #"Food"
monthy1 = float(input("Enter Item 1 Monthly Amount: ")) #133
yearly1 = monthy1*12 #1596
item2 = input("Enter Item 2: ") #"Gas"
monthy2 = float(input("Enter Item 2 Monthly Amount: ")) #53
yearly2 = monthy2*12 #636
item3 = input("Enter Item 3: ") #"Phone"
monthy3 = float(input("Enter Item 3 Monthly Amount: ")) #13
yearly3 = monthy3*12 #156
item4 = input("Enter Item 4: ") #"Utilities"
monthy4 = float(input("Enter Item 4 Monthly Amount: ")) #40
yearly4 = monthy4*12 #480
item5 = input("Enter Item 5: ") #"Credit"
monthy5 = float(input("Enter Item 5 Monthly Amount: ")) #333
yearly5 = monthy5*12 #3996
item6 = input("Enter Item 6: ") #"Medical inshurance"
monthy6 = float(input("Enter Item 6 Monthly Amount: ")) #15
yearly6 = monthy6*12 #180

print ("""
Personal Budget
========================================
 Income             Month       Year
========================================
                    $%-10.2f $%-10.2f
========================================
 Expences           Month       Year
========================================
%-19s $%-10.2f $%-10.2f
%-19s $%-10.2f $%-10.2f
%-19s $%-10.2f $%-10.2f
%-19s $%-10.2f $%-10.2f
%-19s $%-10.2f $%-10.2f
%-19s $%-10.2f $%-10.2f
%-19s $%-10.2f $%-10.2f
%-19s $%-10.2f $%-10.2f
========================================
 Savings            Month       Year
========================================
                    $%-10.2f $%-10.2f""" % (moneyEarned, moneyEarned*12
, "Tithing", moneyEarned*0.1, moneyEarned*1.2
, "Fast offering", fastOffering, fastOffering*12
, item1, monthy1, yearly1
, item2, monthy2, yearly2
, item3, monthy3, yearly3
, item4, monthy4, yearly4
, item5, monthy5, yearly5
, item6, monthy6, yearly6
, savings(moneyEarned, fastOffering, monthy1, monthy2, monthy3, monthy4, monthy5, monthy6)
, savings(moneyEarned, fastOffering, monthy1, monthy2, monthy3, monthy4, monthy5, monthy6)*12))