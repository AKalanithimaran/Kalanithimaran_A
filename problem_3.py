# Conditional odd number pattern
x = int(input("Enter a number: "))

# If x is even → limit = x - 1, else = x
limit = x if x % 2 != 0 else x - 1

series = [2 * i + 1 for i in range(limit)]
print("Output:", ", ".join(map(str, series)))
