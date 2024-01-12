def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print('true')
        return True
      else:
        print('false')
        return False
    else:
      print('true')
      return True
  else:
    print('false')
    return False
  
# TODO: Add more code here 👇
def days_in_month(inputYear, inputMonth):
  '''
  This function takes a Year and Month as inputs and returns if it 
  is a leap year or not and number of days in the month specified.
  '''
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  leapOrNot = is_leap(inputYear)
  numOfDays = month_days[inputMonth -1]
  if leapOrNot == True : 
    month_days[1] = 29
  if leapOrNot == True:
      return f'{inputYear} is a leap year and the {inputMonth}nd month has {month_days[inputMonth -1]} '
  else:
      return f'{inputYear} is not a leap year and the {inputMonth}nd month has {month_days[inputMonth -1]} '
  
#🚨 Do NOT change any of the code below 
year = int(input('enter a year : ')) # Enter a year
month = int(input('enter number of month : ')) # Enter a month
days = days_in_month(year, month)
print(days)
