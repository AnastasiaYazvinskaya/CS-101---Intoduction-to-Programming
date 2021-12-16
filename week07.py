score = float(input("What was your score: ")) # 97, 88, 75, 61
grade = ""

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

print ("For a score of %.2f, your grade is a %s" % (score, grade))