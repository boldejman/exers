def in_seg(a, n, puz):   # checks if a in n-th segment
    for i in range(n // 3 * 3, n // 3 * 3 + 3):
        for j in range(n % 3 * 3, n % 3 * 3 + 3):
            if puz[i][j] == a:
                return True

    return False

def in_lines(a, i, j, puz):   # checks if a in i-th raw or j-th column
    for k in range(9):
        if puz[i][k] == a:
            return True

        if puz[k][j] == a:
            return True

    return False

def zeros(n, puz):   # returns zeros coordinates
    zero = []
    for i in range(n // 3 * 3, n // 3 * 3 + 3):
        for j in range(n % 3 * 3, n % 3 * 3 + 3):
            if puz[i][j] == 0:
                zero.append([i, j])
    return zero

def are_zeros(puz):   # checks if sudoku has zeros
    for i in range(9):
        if zeros(i, puz) != []:
                return True
    return False

def possible_to_set(a, n, i, j, puz):  # checks if a number fit in the position
    if in_seg(a, n, puz):
        return False

    for k in zeros(n, puz):
        if k != [i, j]:
            if not in_lines(a, k[0], k[1], puz):
                return False

    return True

def set_numbers(n, puz): # set numbers in positions
    for i in zeros(n, puz):
        for number in range(1,10):
            if possible_to_set(number, n, i[0], i[1], puz):
                puz[i[0]][i[1]] = number
    return puz


def sudoku(puzzle):   # main function
    while are_zeros(puzzle):
        for i in range(9):
            puzzle = set_numbers(i, puzzle)

    return puzzle


puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

print(sudoku(puzzle))


