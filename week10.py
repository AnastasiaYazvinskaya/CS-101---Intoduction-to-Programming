import random

num = random.randint(1, 75)
guess = int(input("Let's play!\nI conceived a number from 1 to 75, try to guess it for a maximum of 7 attemptes.\nGuess it: "))
attempt = 1

while True:
  if guess > num:
    print ("Nope! That is too high.")
  elif guess < num:
    print ("Nope! That is too low.")
  else:
    print ("Yes! That is my number!\nYou guessed it in %d attemptes.") % (attempt)
    if attempt > 7:
      print ("It seems you did not choose the best tactics, you could guess faster.")
    elif attempt < 7:
      print ("You're lucky since it took you less than 7 attempts to guess my number.")
    else:
      print ("Good job!")
    break
  guess = int(input("Try again: "))
  attempt += 1