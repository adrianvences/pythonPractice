'''
CodeWars
Complete the solution so that the function will break up camel casing, using a space between words.
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
'''


def solution(s):

    list = [x for x in s]

    for char in list:
        if char != list[0] and char.isupper():
            list[list.index(char)] = ' ' + char

    fin_list = ''.join(list).split(' ')
    result = ''
    for word in fin_list:
        result += word + ' '
    
    return result[:-1]
    