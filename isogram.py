
st = 'moOse'

def is_isogram(string):
    dict = {}
    stringLower = string.lower()
    if len(string) == 0:
        return True
    else:
        for letter in stringLower:
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1
        for key in dict:
            if  dict[key] > 1:
                return False
        return True
is_isogram(st)

