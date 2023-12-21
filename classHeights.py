# Input a Python list of student heights
# student_heights = input().split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇

student_heights = [180, 124, 165, 173, 189, 169, 146]

studentHeightSum = 0 

studentCount = 0

averageStudentHeight = 0

for student in student_heights:
  studentHeightSum += student
  # print(studentHeightSum)
  studentCount += 1
  # print(studentCount)
averageStudentHeight = studentHeightSum / studentCount
print(f"the average height in the class is {averageStudentHeight}")

