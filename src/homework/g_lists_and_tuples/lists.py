def get_lowest_list_value(numbers):
    if not numbers:
        return None
    
    lowest = numbers[0]
    for num in numbers:
        if num < lowest:
            lowest = num
    return lowest

def get_highest_list_value(numbers):
    if not numbers:
        return None
    
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest