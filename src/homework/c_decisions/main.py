from decisions import get_options_ratio, get_faculty_rating

def main():
    options = float(input("Enter options: "))
    total = float(input("Enter total: "))
    result = get_options_ratio(options, total)
    rating = get_faculty_rating(result)
    print(f"Faculty Rating: {rating}")

if __name__ == "__main__":
    main()