# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = 8, 5
matrix = [[0 for x in range(w)] for y in range(h)] 
matrix[1][2] = 1
matrix[2][2] = 1
matrix[2][3] = 1
matrix[0][3] = 1

for i in range (0,h):
    for j in range (0,w):
        print(matrix[i][j], end="")
    print()
