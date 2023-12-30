string = 'hello my name is adrian and i am a plumber'

def findShort(string):
  shortestWord = float('inf')
  stringSplit = string.split()
  for word in stringSplit:
    if len(word) < shortestWord :
      shortestWord = len(word)
    
  print(shortestWord)

findShort(string)