one = ['adrian']
two = ['adrian', 'xiomara']
three = ['adrian','xiomara','gen']
four = ['adrian','xiomara','gen','chris']
five = ['adrian','xiomara','gen','chris','mum']
six = ['adrian','xiomara','gen','chris','mum','dad']

def likes(names):
    # your code here
    if len(names) == 0:
        print('no one likes this')
    elif len(names) == 1:
        print(f'{names[0]} likes this')
    elif len(names) == 2:
        print(f'{names[0]} and {names[1]} like this')
    elif len(names) == 3:
        print(f'{names[0]}, {names[1]} and {names[2]} like this')
    elif len(names) > 3 :
        print(f'{names[0]}, {names[1]} and {len(names)-2} others like this')

likes(one)
likes(two)
likes(three)
likes(four)
likes(five)
likes(six)