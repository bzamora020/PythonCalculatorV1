while True:
    print("\nOptions:")
    print("Enter 'add' to add two digits")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to multiply two numbers")
    print("To finish the program enter 'quit' \n")

    enter1 = "Enter your first number:"
    enter2 = "Enter your second number:"
    decision = input("What would you like to do?: ")

    if decision == "add" :
        print(enter1)
        num1 = float(input(""))
        print(enter2)
        num2 = float(input(""))
        result = float(num1 + num2)
        print("The result is " + "%.2f" %result)
        print("")

    elif decision == "subtract" :
        print(enter1)
        num1 = float(input(""))
        print(enter2)
        num2 = float(input(""))
        result = float(num1 - num2)
        print("The result is " + "%.2f" %result)
        print("")

    elif decision == "multiply" :
        print(enter1)
        num1 = float(input(""))
        print(enter2)
        num2 = float(input(""))
        result = float(num1 * num2)
        print("The result is " + "%.2f" %result)
        print("")

    elif decision == "divide" :
        print(enter1)
        num1 = float(input(""))
        print(enter2)
        num2 = float(input(""))
        result = float(num1 / num2)
        print("The result is " + "%.2f" %result)
    elif decision == "quit" :
        break