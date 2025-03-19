def get_hamming_distance(dna1, dna2):
    """
    Calculate the Hamming distance between two DNA strings of equal length.
    Args:
        dna1 (str): First DNA string
        dna2 (str): Second DNA string
    Returns:
        int: The Hamming distance between the two strings
    """
    if len(dna1) != len(dna2):
        return 0
    
    distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance += 1
    return distance

def get_dna_complement(dna):
    """
    Get the reverse complement of a DNA string.
    Args:
        dna (str): The DNA string
    Returns:
        str: The reverse complement of the DNA string
    """
    complement = ""
    # First create the complement
    for char in dna:
        if char == 'A':
            complement += 'T'
        elif char == 'T':
            complement += 'A'
        elif char == 'C':
            complement += 'G'
        elif char == 'G':
            complement += 'C'
    
    # Then reverse it
    reverse_complement = ""
    for i in range(len(complement)-1, -1, -1):
        reverse_complement += complement[i]
    
    return reverse_complement