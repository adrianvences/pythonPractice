str1 = 'rkqodlw' 
str2 = 'world'

def scramble(s1, s2):
    count = 0
    for letter in s1:
        if letter in s2:
            count += 1
            print('yes')
        else :
          print("no")
    if count == len(s2):
      return True
    else:
      return False
        
scramble(str1, str2)