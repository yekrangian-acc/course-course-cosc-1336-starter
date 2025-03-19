from strings import get_hamming_distance, get_dna_complement

def display_menu():
    print("\n1-Hamming Distance")
    print("2-DNA Complement")
    print("3-Exit")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-3): ")

        if choice == '1':
            dna1 = input("Enter first DNA string: ")
            dna2 = input("Enter second DNA string: ")
            result = get_hamming_distance(dna1, dna2)
            print(f"\nHamming Distance: {result}")
        
        elif choice == '2':
            dna = input("Enter DNA string: ")
            result = get_dna_complement(dna)
            print(f"\nDNA Complement: {result}")
        
        elif choice == '3':
            print("\nGoodbye!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == '__main__':
    main()