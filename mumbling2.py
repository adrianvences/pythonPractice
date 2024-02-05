def mumbling(s):
  index = 1 
  result = []
  for char in s:
    letter = char * index
    letter = letter.capitalize()
    index += 1 
    result.append(letter)
  return '-'.join(result)