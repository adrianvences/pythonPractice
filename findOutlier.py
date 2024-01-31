
nums = [1,1,1,2,1]

def find_outlier(integers):
    countOdd = 0
    countEven = 0
    for char in integers:
        if char % 2 == 0:
            countEven += 1 
        else:
            countOdd += 1 
    if countEven == 1 :
      for num in integers:
        if num % 2 == 0:
          print(num)
    elif countOdd == 1:
      for num in integers:
        if num % 2 == 1:
          print(num)          
        
    

find_outlier(nums)

# 90s de toilet,campana 3x4, 5 2" ptrap, tapas de 4, 5 ys de 4, 45s de 4 una caja, pintura, 16 de 4". 