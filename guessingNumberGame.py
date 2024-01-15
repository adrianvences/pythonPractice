print("Welcome to the number guessing game!")
print('im thinking of a number between 1 and 100.')

import random 
randomNumber = random.randint(1,100)
print(randomNumber)
level = input('Choice a difficulty. Type "easy" or "hard" : ')
lives = 0
if level == "hard":
  lives += 10
else:
  lives +=5
print(f'You have {lives} attempts remaining to guess the number.')

# guess = int(input('make a guess : '))
def guessing():
  while lives > 0:
    guess = int(input('make a guess : '))
    if guess > randomNumber:
      lives -= 1
      if lives == 0:
        return print('you have run out of lives. try again')
      else:
        print("To high. Guess Again")
        print(f'you have {lives} remaining.')
    elif guess < randomNumber:
      lives -= 1
      if lives == 0:
        return print('you have run out of lives. try again')
      else:
        print('Too low. Guess Again.')
        print(f'you have {lives} remaining.')
    else:
      return print('Got it! thats correct! Good Job!')
guessing()