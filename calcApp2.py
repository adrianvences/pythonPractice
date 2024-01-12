

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
def calculator():
  num1 = float(input('What is the first number? : '))
  for symbol in dictOfFunctions:
    print(symbol)
  continueOrNot = True

  while continueOrNot:
    operationSymbol = input('pick and operation from the line above. : ')
    num2 = float(input('What is the second number? : '))
    calculation_function = dictOfFunctions[operationSymbol]
    answer = calculation_function(num1,num2)

    print(f'{num1} {operationSymbol} {num2} = {answer}')

    if input(f" Type 'y' to continue calculating with {answer} , or type 'n' to start a new calculation.") == 'y':
      num1 = answer
    else:
      continueOrNot = False
      calculator()
calculator()