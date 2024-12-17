w = 8
h = 5

def get_empty_matrix(w, h):
    matrix = [[0 for x in range(w)] for y in range(h)] 
    return matrix

def set_matrix_to_contain_glider(matrix):
    matrix[1][2] = 1
    matrix[2][2] = 1
    matrix[2][3] = 1
    matrix[0][3] = 1
    return matrix

def print_matrix(matrix):
    for i in range (0,h):
        for j in range (0,w):
            print(matrix[i][j], end="")
        print()

# Creates a list containing 5 lists, each of 8 items, all set to 0
matrix = get_empty_matrix(w, h)
matrix = set_matrix_to_contain_glider(matrix)
print_matrix(matrix)
