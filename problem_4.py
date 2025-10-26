# Get total count of numbers in list which are multiples of [1–9]
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = {}

for i in range(1, 10):
    count = sum(1 for n in numbers if n % i == 0)
    result[i] = count

print("Output:", result)
