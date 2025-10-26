# Generate odd number series till x
x = int(input("Enter a number: "))

# Generate odd numbers till n
series = [2 * i + 1 for i in range(x)]
print("Output:", ", ".join(map(str, series)))
