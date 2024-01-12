num = 'MMMCMXCIX'
# 3999

'''
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

'''

romanDict = {
"I" : 1,
"V" : 5,
"X" : 10,
"L" : 50,
"C" : 100,
"D" : 500,
"M" : 1000
}

intList = []



def romanTrans(romanNum):
  intTranslation = 0
  """complete the solution by transforming the roman numeral into an integer"""
  for letter in romanNum: 
    
    intList.append(romanDict[letter])
    # print(romanDict[letter])
    print(intList)
  for num in intList:
    previousNum = num
    
    if num > previousNum:
      intTranslation -= num
    else:
      intTranslation+=num
      print(intTranslation)

romanTrans(num)