score = [] # 97, 63, 74, 81, 89
overageScore = 0

for i in range(5):
  score.append(float(input("What was your score: ")))
  overageScore += score[i] 
grade = ""

overageScore /= 5 # 80.8

if overageScore >= 93:
  grade = "A"
elif overageScore >= 90:
  grade = "A-"
elif overageScore >= 87:
  grade = "B+"
elif overageScore >= 83:
  grade = "B"
elif overageScore >= 80:
  grade = "B-"
elif overageScore >= 77:
  grade = "C+"
elif overageScore >= 73:
  grade = "C"
elif overageScore >= 70:
  grade = "C-"
elif overageScore >= 67:
  grade = "D+"
elif overageScore >= 63:
  grade = "D"
elif overageScore >= 60:
  grade = "D-"
else:
  grade = "F"

print ("For a overageScore of %.2f, your grade is a %s" % (overageScore, grade))