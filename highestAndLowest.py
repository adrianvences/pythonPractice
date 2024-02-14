nums = ("8 3 -5 42 -1 0 0 -9 4 7 4 -4")

def high_and_low(numbers):
    numbersSplit = numbers.split()
    realNumbers = []
    for num in numbersSplit:
        realNumbers.append(int(num))
    result = f'{max(realNumbers)}, {min(realNumbers)}'
    print(result)
high_and_low(nums)