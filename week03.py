item1 = "Food"
yearly1 = 1600
monthy1 = yearly1/12.
item2 = "Gas"
yearly2 = 640
monthy2 = yearly2/12.
item3 = "Phone"
yearly3 = 160
monthy3 = yearly3/12.
item4 = "Utilities"
yearly4 = 480
monthy4 = yearly4/12.
item5 = "Credit"
yearly5 = 4000
monthy5 = yearly5/12.
item6 = "Medical inshurance"
yearly6 = 185
monthy6 = yearly6/12.

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