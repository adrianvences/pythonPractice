import math
# Write your code below this line 👇
def paint_calc(height,width,cover):
  numberOfCans = math.ceil((height*width) / cover)

  print(f"youll need {numberOfCans} cans of paint")



# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("what is the height of the wall?\n")) # Height of wall (m)
test_w = int(input("what is the width of the wall?\n")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)