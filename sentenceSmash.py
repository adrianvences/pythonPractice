def smash(words):
    sentence = ' '.join(words)
    return sentence

def smash(words):
    sentence = ''
    for word in words:
        sentence += ' ' + word
    return sentence[1:]