import random

debug = False
w = 40
h = 20

# Creates a list containing 5 lists, each of 8 items, all set to 0
def get_empty_matrix(w, h):
    matrix = [[0 for y in range(h)] for x in range(w)] 
    return matrix

def set_matrix_to_contain_glider(matrix):
    matrix[3][12] = 1
    matrix[4][12] = 1
    matrix[4][13] = 1
    matrix[4][14] = 1
    matrix[2][13] = 1
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
        potential_neighbors.pop()
        potential_neighbors.pop()
        potential_neighbors.pop()
        # skip neighbors after right side
        if debug:
            print("potential neighbors after popping x+1s: ")
            print(potential_neighbors)
    if coords[1] == 0:
    # location is on y==0
        potential_neighbors.remove([x,y-1])
        if [x-1,y-1] in potential_neighbors:
            potential_neighbors.remove([x-1,y-1])
        if [x+1,y-1] in potential_neighbors:
            potential_neighbors.remove([x+1,y-1])
        # skip neighbors before first row
    elif coords[1] == h-1:
        potential_neighbors.remove([x,y+1])
        if [x-1,y+1] in potential_neighbors:
            potential_neighbors.remove([x-1,y+1])
        if [x+1,y+1] in potential_neighbors:
            potential_neighbors.remove([x+1,y+1])
        # skip neighbors after last row
    if debug:
        print("potential neighbors after popping ys: ")
        print(potential_neighbors)

        print("For cell ", end="")
        print(coords)
    for neighbor in potential_neighbors:
        if debug:
            print([neighbor[0]], [neighbor[1]])
            print(matrix[neighbor[0]][neighbor[1]])
        if matrix[neighbor[0]][neighbor[1]] == 1:
            count += 1
    if debug:
        print("Sum: ", count)
    return count

def calculate_next_round_matrix(matrix):
    new_matrix = get_empty_matrix(w, h)
    for i in range (0,h):
        for j in range (0,w):
            n = calculate_neighbors(matrix, [j, i], w, h)
            if (matrix[j][i] == 1):
                #alive previously
                if (n == 2 or n == 3):
                    #generate cell's value as 1 next round
                    new_matrix[j][i] = 1
                else:
                    #generate cell's value as 0 next round    
                    new_matrix[j][i] = 0                    
            else:
                #dead previously
                if n == 3:
                    #generate cell's value as 1 next round
                    new_matrix[j][i] = 1
                else:
                    #generate cell's value as 0 next round    
                    new_matrix[j][i] = 0
    return new_matrix

def print_matrix(matrix):
    for i in range (0,h):
        for j in range (0,w):
            print(matrix[j][i], end="")
        print()

matrix = get_empty_matrix(w, h)
matrix = set_matrix_to_contain_glider(matrix)
print_matrix(matrix)
input_value = ""
while input_value != "q":
    input_value = input("Enter to continue / enter 'q' to quit> ")
    matrix = calculate_next_round_matrix(matrix)
    print_matrix(matrix)