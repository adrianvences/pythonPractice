import random

from hangman_words import wordList
from hangman_art import stages,logo

print(logo)
word = ''
display = []
endOfGame = False
lives = 6


word = random.choice(wordList)

# print(f"heres a hint {word}")

wordLength = len(word)
for char in word:
  display.append("_")

print(display)

while endOfGame == False:
  guess = input("Pick a letter?\n").lower()
  if guess in display:
    print(f'you have already chosen : {guess}')
  for position in range(wordLength):
    letter = word[position]
    if letter == guess:
      # display.insert(word.index(position),guess)
      display[position] = letter
      print(display)

  if guess not in word:
    print(f'the letter {guess} is not in the word. you lose a point.')
    lives -= 1   
    print(stages[lives+1])

    # if guess in display:
    #   print(f'Oops, you have already guessed "{guess}"')

    if lives < 0:
      endOfGame = True
      print('you lose')

  if "_" not in display:
        endOfGame = True
        print("You win.")
      # list.insert(index, elem)