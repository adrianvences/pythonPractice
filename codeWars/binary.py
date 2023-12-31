n = 7
def count_bits(n):
  binaryRepp = bin(n)[2:]
  print(binaryRepp)
  count=0
  for num in binaryRepp:
    num = int(num)
    if num % 2 != 0:
      count+=1
  print(count) 
count_bits(n)