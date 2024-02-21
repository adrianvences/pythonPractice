test = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]

def open_or_senior(data):
    result = []
    for inner_list in data:

      if inner_list[0] > 54 and inner_list[1] > 7:
              
        result.append('Senior')
      else:
        result.append('Open')
    print(result)

open_or_senior(test)