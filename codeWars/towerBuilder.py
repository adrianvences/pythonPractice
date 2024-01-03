def tower_builder(n_floors):
  if n_floors == 0:
    return []
  
  count = 1
  result = []

  for i in range(1,n_floors + 1):
    print(i)
    stars = '*' * (2 * i - 1)
    print(stars)
    space = " " * (n_floors - i)
    print(space)
    result.append(space + stars +space)
    print(result)
  
  return result

tower_builder(10)