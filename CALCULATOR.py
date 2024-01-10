while True:   
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1,2,3,4,5): ")
   
    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print("Result: ", result)
        
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print("Result: ", result)
        
    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print("Result: ", result)
        
    elif choice == '4':
        num1 = float(input("Enter dividend: "))
        num2 = float(input("Enter divisor: "))
        if num2 != 0:
            result = num1 / num2
            print("Result: ", result)
        else:
            print("Error: Cannot divide by zero.")
    elif choice == '5':
        print("Invalid Input")
        break