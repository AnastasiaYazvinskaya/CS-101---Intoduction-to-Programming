item1 = input("Enter Item 1: ") #"Food"
monthy1 = float(input("Enter Item 1 Monthly Amount: ")) #133.33
yearly1 = monthy1*12 #1600
item2 = input("Enter Item 2: ") #"Gas"
monthy2 = float(input("Enter Item 2 Monthly Amount: ")) #53.33
yearly2 = monthy2*12 #640
item3 = input("Enter Item 3: ") #"Phone"
monthy3 = float(input("Enter Item 3 Monthly Amount: ")) #13.33
yearly3 = monthy3*12 #160
item4 = input("Enter Item 4: ") #"Utilities"
monthy4 = float(input("Enter Item 4 Monthly Amount: ")) #40
yearly4 = monthy4*12 #480
item5 = input("Enter Item 5: ") #"Credit"
monthy5 = float(input("Enter Item 5 Monthly Amount: ")) #333.33
yearly5 = monthy5*12 #4000
item6 = input("Enter Item 6: ") #"Medical inshurance"
monthy6 = float(input("Enter Item 6 Monthly Amount: ")) #15.42
yearly6 = monthy6*12 #185

print ("""Monthly Budget
=========================================
 Item                Month       Year
=========================================
%-20s $%-10.2f $%-10.2f
%-20s $%-10.2f $%-10.2f
%-20s $%-10.2f $%-10.2f
%-20s $%-10.2f $%-10.2f
%-20s $%-10.2f $%-10.2f
%-20s $%-10.2f $%-10.2f""" % (item1, monthy1, yearly1, item2, monthy2, yearly2,
item3, monthy3, yearly3, item4, monthy4, yearly4, item5, monthy5, yearly5,
item6, monthy6, yearly6,))