def get_p_distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Sequences must be of equal length")
    
    differences = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            differences += 1
    
    return differences / len(list1)

def get_p_distance_matrix(sequences):
    n = len(sequences)
    matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = get_p_distance(sequences[i], sequences[j])
            else:
                matrix[i][j] = 0.0
    
    return matrix 