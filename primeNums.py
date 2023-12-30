# Write your code below this line 👇
def prime_checker(n):
  
  if n <= 1 :
      return print('number is not a prime number')
  
  for i in range(2,n):
    if n % i == 0 :
      return print('this is not a prime number')
    else:
      return print('this is a prime number')
# Write your code above this line 
#Do NOT change any of the code below👇
n = int(input('Input a number to check if it is prime or not : ')) # Check this number
prime_checker(n)