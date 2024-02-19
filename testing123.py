test = ['a','b','c']

def number(lines):
    result = []
    num = 0
    for char in lines:
        num+=1
        result.append(f'{num}: {char}')
    print(result)
number(test)