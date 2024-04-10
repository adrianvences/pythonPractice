"""
CodeWars
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
"""

def double_char(s):
    res = ''
    for char in s:
        res += char * 2
    return res