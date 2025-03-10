from repetition import get_factorial, sum_odd_numbers

def display_menu():
    print("\nHomework 3 Menu")
    print("1-Factorial")
    print("2-Sum odd numbers")
    print("3-Exit")

def get_valid_number(prompt, min_val, max_val):
    while True:
        try:
            num = int(input(prompt))
            if min_val <= num <= max_val:
                return num
            print(f"Number must be between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def continue_program():
    while True:
        choice = input("\nDo you want to continue? (y/n): ").lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Invalid input. Please enter 'y' or 'n'.")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice (1-3): "))
            
            if choice == 1:
                num = get_valid_number("Enter a number for factorial (1-9): ", 1, 9)
                result = get_factorial(num)
                print(f"\nThe factorial of {num} is: {result}")
                if not continue_program():
                    break
                    
            elif choice == 2:
                num = get_valid_number("Enter a number for sum of odd numbers (1-99): ", 1, 99)
                result = sum_odd_numbers(num)
                print(f"\nThe sum of odd numbers up to {num} is: {result}")
                if not continue_program():
                    break
                    
            elif choice == 3:
                if continue_program():
                    continue
                break
                
            else:
                print("\nInvalid choice. Please select 1, 2, or 3.")
                
        except ValueError:
            print("\nInvalid input. Please enter a number.")

if __name__ == "__main__":
    main()