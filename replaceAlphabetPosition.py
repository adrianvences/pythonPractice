
string = 'abcdefghaijklmanopqrstuvwxyza'

def alphabet_position(text):

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    emptyString = ''
    
    for char in text.lower():
        if char.lower() in alphabet:
            position = (alphabet.index(char)+1)
            emptyString += str(position) + " "
    return print(emptyString)

alphabet_position(string)