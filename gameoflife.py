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

def calculate_neighbors(matrix, coords, w, h):
    x = coords[0]
    y = coords[1]
    potential_neighbors = [[x-1,y-1],[x-1,y],[x-1,y+1],[x,y-1],[x,y+1],[x+1,y-1],[x+1,y],[x+1,y+1]]
    count = 0
    if coords[0] == 0:
    # location is on x==0
        potential_neighbors.pop(0)
        potential_neighbors.pop(0)
        potential_neighbors.pop(0)
        # skip neighbors before left side
    elif coords[0] == w-1:
        porential_neighbors.pop()
        porential_neighbors.pop()
        porential_neighbors.pop()
        # skip neighbors after right side
    if coords[1] == 0:
    # location is on y==0
        potential_neighbors.remove([x,y-1])
        # skip neighbors before first row
    elif coords[1] == h-1:
        potential_neighbors.remove([x,y+1])
        # skip neighbors after last row
    count = len(potential_neighbors)
    return count

def calculate_next_round_matrix(matrix):
    for i in range (0,h):
        for j in range (0,w):
            n = calculate_neighbors(matrix, [j,i], w, h)
            if n == 3 or n == 4
                #generate cell's value as 1 next round
                pass
            else:
                #generate cell's value as 0 next round    
                pass

def print_matrix(matrix):
    for i in range (0,h):
        for j in range (0,w):
            print(matrix[i][j], end="")
        print()

# Creates a list containing 5 lists, each of 8 items, all set to 0
matrix = get_empty_matrix(w, h)
matrix = set_matrix_to_contain_glider(matrix)
print_matrix(matrix)
