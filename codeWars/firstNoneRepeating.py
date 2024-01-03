

string = 'letteR'
def first_non_repeating_letter(s):
  cloneString = string.lower()
  countDictionary = {}
  for i in range(len(string)):
    if not cloneString[i] in countDictionary:
      countDictionary[i] = 1
    else:
      countDictionary += 1
    print(countDictionary)    
  


first_non_repeating_letter(string)