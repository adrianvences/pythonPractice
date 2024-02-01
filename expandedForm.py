number = 10500

def expandedForm(num):
  stringNum = str(num)
  st = ''

  for num in stringNum:
    if num != '0':

      numOfZeros = len(stringNum) - stringNum.index(num)-1
      zeros = numOfZeros * '0'
      st += num + zeros + '+'
    
    # next to figure out how to get rid of '+' at end of the string

  # print(st)



expandedForm(number)