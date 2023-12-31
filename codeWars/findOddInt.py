seq = [1,3,3,1,4,4,6,5,6]
def findIt(seq):
  for num in seq:
    a = seq.count(num)
    if a % 2 == 0:
      continue
    print(num)
    return num

findIt(seq)