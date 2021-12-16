import math

def displayWelcome():
  print ("""Welcome to my area and perimeter calculator
============================================""")

def calcAreaCircle(radius):
  a = math.pi*radius**2
  return a

def calcPerimeterCircle(radius):
  l = 2*math.pi*radius
  return l

def calcAreaSquare(side):
  a = side**2
  return a

def calcPerimeterSquare(side):
  p = side*4
  return p

def calcAreaRect(width, height):
  a = width*height
  return a

def calcPerimeterRect(width, height):
  p = (width + height)*2
  return p

def calcAreaTriangle(base, height):
  a = base*height/2
  return a

displayWelcome()


radius = 3.56

area = calcAreaCircle(radius)

perimeter = calcPerimeterCircle(radius)

print('Circle   : area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


side = 9.23

area = calcAreaSquare(side)

perimeter = calcPerimeterSquare(side)

print('Square   : area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


width = 2.9

height = 14.22

area = calcAreaRect(width, height)

perimeter = calcPerimeterRect(width, height)

print('Rectangle: area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


base = 7.97

height = 5.31

area = calcAreaTriangle(base, height)

print('Triangle : area = {0:.2f}'.format(area))