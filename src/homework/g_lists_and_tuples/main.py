from lists import get_lowest_list_value, get_highest_list_value

def get_user_numbers():
    numbers = []
    while True:
        try:
            value = float(input("Enter a list value: "))
            numbers.append(value)
            
            if len(numbers) >= 3:
                response = input("Do you want to enter another value? (y/n): ")
                if response.lower() != 'y':
                    break
        except ValueError:
            print("Please enter a valid number.")
    return numbers

def main():
    while True:
        print("\nMenu:")
        print("1. Show the list low/high values")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == '1':
            numbers = get_user_numbers()
            if numbers:
                lowest = get_lowest_list_value(numbers)
                highest = get_highest_list_value(numbers)
                print(f"\nLowest value: {lowest}")
                print(f"Highest value: {highest}")
            else:
                print("No numbers were entered.")
        
        elif choice == '2':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()