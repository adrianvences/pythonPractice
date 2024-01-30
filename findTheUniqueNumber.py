arr = [ 1, 1, 1, 2, 1, 1 ] 
arr2 = [ 0, 0, 0.55, 0, 0 ]

# There is an array with some numbers. All numbers are equal except for one. Try to find it!

def find_uniq(array):
    numbers = {}
    for num in array:
      if num not in numbers:
        numbers[num] = 0
      numbers[num] += 1
    for key in numbers:
      if numbers[key] ==1:
        print(key)

find_uniq(arr)