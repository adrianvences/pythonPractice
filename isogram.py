
st = 'hello'

def is_isogram(string):
    dict = {}
    flag = True
    stringLower = string.lower()
    for letter in stringLower:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1
    for key in dict:
        if  dict[key] > 1:
            return False
        else: 
            return True

is_isogram(st)

# not done###############