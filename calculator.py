def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiple(x, y):
    return x * y

def division(x, y):
    return x / y

print("Welcome to the state of the art calculator!\n")
print("What are doing?\n")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operator = input("\nPick a number from the list above: ")

num_1 = input("\nPlese input the first number: ")
num_2 = input("Please input the second number: ")

if operator == '1':
    print(num_1, "+",num_2,"=", add(num_1,num_2))