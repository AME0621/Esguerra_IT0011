import os

# Clear Screen (CLS) 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Divide
def divide(num1, num2):
    if num2 == 0:
        return None  
    return num1 / num2

# Exponentiation
def exponentiation(base, exponent):
    return base ** exponent

# Remainder
def remainder(num1, num2):
    if num2 == 0:
        return None 
    return num1 % num2

# Summation
def summation(start, end):
    if end <= start:
        return None  
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

# Operation Menu
def menu():
    while True:
        clear_screen() 

        print("\n========================")
        print("   * OPERATION MENU *   ")
        print("========================")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        print("------------------------")
        choice = input("Enter your choice: ").upper()

        if choice == 'Q':
            print("\nExiting program...")
            break

        if choice == 'D':
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            result = divide(num1, num2)
            if result is None:
                print("Error: Cannot divide by zero!")
            else:
                print(f"\nResult: {result}")

        elif choice == 'E':
            base = float(input("\nEnter base number: "))
            exponent = float(input("Enter exponent: "))
            result = exponentiation(base, exponent)
            print(f"\nResult: {result}")

        elif choice == 'R':
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            result = remainder(num1, num2)
            if result is None:
                print("\nError: Cannot calculate remainder with zero as the second number!")
            else:
                print(f"\nResult: {result}")

        elif choice == 'F':
            start = int(input("\nEnter the starting number: "))
            end = int(input("Enter the ending number: "))
            result = summation(start, end)
            if result is None:
                print("\nError: The second number must be greater than the first!")
            else:
                print(f"\nResult: {result}")

        else:
            print("\nInvalid choice, please try again.")

        input("\nPress Enter to continue...")

# Start the menu
if __name__ == "__main__":
    menu()
