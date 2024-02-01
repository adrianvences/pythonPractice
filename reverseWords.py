stringg = 'hello my name is Adrian.'

def reverse_words(text):
    newString = text.split(" ")
    reverseWords = ''
    for word in newString:
      reverseWords += word[::-1] + ' '
      print(reverseWords)
    


reverse_words(stringg)