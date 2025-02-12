#TME number 1

def is_palindrome(num):
    """Check if a number is a palindrome."""
    return str(num) == str(num)[::-1]

try:

    with open('TMA/numbers.txt', 'r') as file:
        line_number = 1
        for line in file:
            numbers = line.strip().split(',')
            
            try:
                total = sum(int(number) for number in numbers)
            except ValueError:
                print(f"Error in line {line_number}: Non-numeric value found.")
                line_number += 1
                continue

            if is_palindrome(total):
                print(f"Line {line_number}: {line.strip()} (sum {total}) - Palindrome")
            else:
                print(f"Line {line_number}: {line.strip()} (sum {total}) - Not a palindrome")
            
            line_number += 1

except FileNotFoundError:
    print("Error: The file 'numbers.txt' was not found in the current directory.")



#TME number 2

def get_month_name (month_number):
    months = {
        "01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August",
        "09": "September", "10": "October", "11": "November", "12": "December"
    }
    return months.get(month_number, "Invalid Month")

date = input("Enter the date (mm/dd/yyyy): ")

month, day, year = date.split('/')

month_name = get_month_name(month)

print(f"Date Output: {month_name} {int(day)}, {year}")


