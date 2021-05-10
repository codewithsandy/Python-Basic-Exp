grocery = ["Sugar", "Pizza", "Ice-Cream", 100]
print(grocery)
print(grocery[1])
numbers = [2, 5, 6, 9, 4]
print(numbers)
print(numbers[3])

print(numbers[0:4])
print(numbers[1:3])
print(numbers[::1])
print("\n")
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

numbers.append(99)
print("\t", numbers)

numbers.insert(1, 1996)
print(numbers)

numbers.pop()
print(numbers)