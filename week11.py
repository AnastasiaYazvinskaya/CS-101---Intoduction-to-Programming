def letter_grade(score):
  if score >= 93:
    grade = "A"
  elif score >= 90:
    grade = "A-"
  elif score >= 87:
    grade = "B+"
  elif score >= 83:
    grade = "B"
  elif score >= 80:
    grade = "B-"
  elif score >= 77:
    grade = "C+"
  elif score >= 73:
    grade = "C"
  elif score >= 70:
    grade = "C-"
  elif score >= 67:
    grade = "D+"
  elif score >= 63:
    grade = "D"
  elif score >= 60:
    grade = "D-"
  else:
    grade = "F"
  return grade

scores = {"Math": 0, "English": 0, "PE": 0, "Science": 0, "Art": 0} #95, 81, 100, 78, 56

for course in scores:
  scores[course] = float(input("Enter the score you recieved for " + course + ": "))
print ("")

for course in scores:
  print ("Your %s score is %.2f, you got a %s") % (course, scores[course], letter_grade(scores[course]))