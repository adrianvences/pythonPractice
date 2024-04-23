'''
CodeWars 
Write a function that takes a single non-empty string 
of only lowercase and uppercase ascii letters (word) as 
its argument, and returns an ordered list containing the
indices of all capital (uppercase) letters in the string.

input ==> output
"CodEWaRs" --> [0,3,4,6]
'''

def capitals(word):
    order = []
    newList = list(word)
    for letter in newList:
        if letter.isupper():
            order.append(newList.index(letter))
    return order
        
