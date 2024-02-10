string = 'AAAABBBCCDAABBB'

def unique_in_order(sequence):
    result = []
    for i in sequence:
      if result == []:
        result.append(i)
      elif result[-1] != i:
        result.append(i)
    print(result)
unique_in_order(string)