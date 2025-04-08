from lists_and_tuples import get_p_distance_matrix

def get_sequence_input():
    sequences = []
    while True:
        sequence = input("Enter a DNA sequence (or 'done' to finish): ").upper()
        if sequence.lower() == 'done':
            break
        sequences.append(list(sequence))
    return sequences

def print_matrix(matrix):
    for row in matrix:
        print(' '.join([f"{val:.5f}" for val in row]))

def main():
    while True:
        print("\nMenu:")
        print("1-Get p distance matrix")
        print("2-Exit")
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            print("\nEnter DNA sequences (A, T, C, G only):")
            sequences = get_sequence_input()
            if len(sequences) < 2:
                print("Please enter at least 2 sequences")
                continue
                
            try:
                matrix = get_p_distance_matrix(sequences)
                print("\nP-distance matrix:")
                print_matrix(matrix)
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '2':
            print("Exiting program...")
            break
            
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()