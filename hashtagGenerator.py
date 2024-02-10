sample = " Hello there thanks for trying my Kata"

def generate_hashtag(s):
    splitString = s.split()
    result = ['#',]
    for word in splitString:
        result += word.capitalize()
    
    result = ''.join(result)
    
    if len(s) == 0 or len(result) > 140:
        return False
    else: return result


generate_hashtag(sample)

#updated if statement to make sure string isnt longer than 140 characters after adding hashtag