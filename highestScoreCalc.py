student_scores = [78, 65, 89, 86, 55, 91, 64, 89,100]

highestScore = 0 

for score in student_scores:
  highestScore = score
  if score > highestScore:
    highestScore = score
  else:
    continue

print(f"the highest score in the class is {highestScore}")