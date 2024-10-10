a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b if b != 0 else "undefined (division by zero)"

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
