from class_a import Die

def main():
    die = Die()
    while True:
        value = die.roll()
        print(f"\n{die}")
        
        choice = input("\nDo you want to roll again? (y/n): ").lower()
        if choice != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()