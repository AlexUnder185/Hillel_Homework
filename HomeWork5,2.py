working_calc = "y"
while working_calc in ("y", "yes"):

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    action = input("What action do you want to take? ")
    if action == "+":
        print(num1 + num2)
    elif action == "-":
        print(num1 - num2)
    elif action == "*":
        print(num1 * num2)
    elif action == "/":
        if num2==0:
            print("You can't divide by zero.")
        else:
            print(num1 / num2)
    working_calc = input('You need a calculator? (y/n): ')