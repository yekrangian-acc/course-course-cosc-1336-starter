from dictionary import add_inventory, remove_inventory_widget

def display_menu():
    print("\nInventory Menu")
    print("1-Add or Update Item")
    print("2-Delete Item")
    print("3-Exit")

def main():
    inventory = {}
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            widget_name = input("Enter widget name: ")
            try:
                quantity = int(input("Enter quantity: "))
                add_inventory(inventory, widget_name, quantity)
                print(f"Updated {widget_name} quantity to {inventory[widget_name]}")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        
        elif choice == '2':
            widget_name = input("Enter widget name to delete: ")
            result = remove_inventory_widget(inventory, widget_name)
            print(result)
        
        elif choice == '3':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()