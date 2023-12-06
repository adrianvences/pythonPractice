classScores = [60,80,50,60,80,85,78,45,95,82,76,82]
myScore = 97

def better_than_average(class_points, your_points):
  average = sum(class_points) / len(class_points)

  if your_points > average:
    return True

  else:
    return False
print(sum(classScores)/5)