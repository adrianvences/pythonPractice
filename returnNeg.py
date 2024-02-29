'''
code wars 
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0
The number can be negative already, in which case no change is required.
Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.

'''

def make_negative( number ):
    num = 0 
    if number <= 0:
        return number 
    else:
        num = num - number
    return num