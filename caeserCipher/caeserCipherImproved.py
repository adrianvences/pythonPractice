alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(inputText,shiftAmount,direction):
  if direction == 'encode':
    cipherText = ''
    for letter in inputText:
      position = alphabet.index(letter)
      new_position = position + shiftAmount
      new_letter = alphabet[new_position]
      cipherText += new_letter
    print(f'the encoded text is {cipherText}')
  
  elif direction == 'decode':
    cipherTextDecrypted = ''
    for letter in inputText:
      position = alphabet.index(letter,25)
      new_position = position - shiftAmount
      new_letter = alphabet[new_position]
      cipherTextDecrypted += new_letter
    print(f'the decrypted cipher is {cipherTextDecrypted}')

caesar(inputText=text,shiftAmount=shift,direction=direction)




