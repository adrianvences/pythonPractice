

# add 
def add(n1,n2):
  return n1 + n2

# subtract
def subtract(n1,n2):
  return n1 - n2 

# multiply
def multiply(n1,n2):
  return n1 * n2 

# divide 
def divide(n1,n2):
  return n1 / n2 

dictOfFunctions = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide

  }

num1 = int(input('What is the first number? : '))
for symbol in dictOfFunctions:
  print(symbol)


operationSymbol = input('pick and operation from the line above. : ')

num2 = int(input('What is the second number? : '))

calculation_function = dictOfFunctions[operationSymbol]
answer = calculation_function(num1,num2)
print(f'{num1} {operationSymbol} {num2} = {answer}')

continueOrNot = input( f' type "y" if you would like to continue calculating with {answer}, or type "n" to exit : ' )

while continueOrNot == 'y' :
  operationSymbol = input('pick and operation from the line above. : ')
  nextNum = int(input('What is the  next number? : '))
  calculation_function = dictOfFunctions[operationSymbol]
  answer2 = calculation_function(answer,nextNum)
  print(f'{answer} {operationSymbol} {nextNum} = {answer2}')
  answer = answer2
  continueOrNot = input( f' type "y" if you would like to continue calculating with {answer2}, or type "n" to exit : ' )