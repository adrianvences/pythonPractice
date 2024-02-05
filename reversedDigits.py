nums = 1234

def digitize(n):
    result = []
    stringOfNums = str(n)
    for num in reversed(stringOfNums):
        result.append(int(num))
    print(result)
digitize(nums)