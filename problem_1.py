# Calculator using Class

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero not allowed"
        return a / b

if __name__ == "__main__":
    calc = Calculator()

    op = input("Enter operation (add/sub/mul/div): ").strip().lower()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if op == "add":
        print("Result:", calc.add(a, b))
    elif op == "sub":
        print("Result:", calc.subtract(a, b))
    elif op == "mul":
        print("Result:", calc.multiply(a, b))
    elif op == "div":
        print("Result:", calc.divide(a, b))
    else:
        print("Invalid operation")
