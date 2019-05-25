
numbers = [3, 5, 7, 9, 10.5]
numbers.append('python')
print(len(numbers))

print(numbers[0])

print(numbers[-1])

print(numbers[0:3])

print(numbers[-2:])

print(numbers[:-2])

numbers.remove('python')
del numbers[-1]

print(numbers)