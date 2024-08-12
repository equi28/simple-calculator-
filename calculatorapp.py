print("select an operation to perform")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("Select an Operation: ")
operation = input()

if operation == "1":
    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print("The sum is " + str(int(num1) + int(num2)))
    # code for add
elif operation == "2":
    # code for subtract
    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print("The difference is " + str(int(num1) - int(num2)))
elif operation == "3":
    # code for multiplication
    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print("The Product is " + str(int(num1) * int(num2)))
elif operation == "4":
    # code for division
    num1 = input("Enter First Number: ")
    num2 = input("Enter Second Number: ")
    print("The Quotient is: " + str(int(num1) / int(num2)))
    
else:
    print("Invalid Entry")