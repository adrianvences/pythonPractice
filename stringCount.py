
string = 'hello'

def count(s):
  count = {}
  for letter in s:
    if letter not in count:
      count[letter] = 1
    else:
      count[letter] += 1
  print(count)

count(string)