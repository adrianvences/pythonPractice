stringg = 'hello my name is Adrian.'

# def reverse_words(text):
#     newString = text.split(" ")
#     reverseWords = ''
#     for word in newString:
#       reverseWords += word[::-1] + '#'
#       print(reverseWords)

def reverse_words(text):
    newString = text.split(' ')
    wordsReversed = ''
    for word in newString:
        wordsReversed +=  word[::-1] + ' '
    return wordsReversed[1:]

# def reverse_words(text):
#     newString = text.split(" ")
#     reverseWords = ''
#     for word in newString:
#         reverseWords += " " + word[::-1]
#     return reverseWords[1:]
    


reverse_words(stringg)