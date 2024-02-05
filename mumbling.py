example = "abcd"
def accum(st):
    string = ''
    stringFinal = ''
    for char in st :
        numOfChars =  st.index(char)+1
        string += '-' + char * numOfChars
    string = string.split('-')
    for word in string:
      stringFinal += '-' + word.capitalize()
      
    print(stringFinal[2:])
    
accum(example)

'N-Yy-Fff-Fff-Sssss-Gggggg-Eeeeeee-Yy-Yy-Llllllllll-Bbbbbbbbbbb'
'N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb'