for n in range(4):
  print ("""=======================================================
What is your shape?""")
  shape = input("Enter C for Circle, T for Triangle, or R for Rectangle. ")
  
  if shape.upper() == "C":
    radius = float(input("Enter the radius: "))
    area = 3.14 * radius ** 2
    print ("Area of circle = " + str(area))
  elif shape.upper() == "T":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = base * height / 2
    print ("Area of triangle = " + str(area))
  elif shape.upper() == "R":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = base * height
    print ("Area of rectangle = " + str(area))
  else:
    print ("You did not enter in a valid option. Try again.")
    continue