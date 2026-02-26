numbers = [23,323,343,23,43,132,1,4,24,1,42,42,1,1,14]

numbers.reverse()

for x in range(len(numbers)):
    for y in range(x + 1, len(numbers)):
        if numbers[x] < numbers[y]:
            numbers[x], numbers[y] = numbers[y], numbers[x]
numbers.reverse()

print(numbers)
