board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]


def solve(bo):

    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):  # Loop thru values 1 - 10
        if valid(bo, i, (row, col)):  # Checks to see i = num is valid for place on board
            bo[row][col] = i  # If valid, adds into board at row, col

            if solve(bo):  # Recursively try to finish solution by constantly calling solve()
                return True

            bo[row][col] = 0  # If solution is not true, backtracks and resets last input/solution

    return False


def valid(bo, num, pos):

    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):

    # Prints Row
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:  # Divides row "i" into sections of 3s
            print("- - - - - - - - - - - ")

        # Prints Column
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):

    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:  # For each spot on board that has "0"
                return (i, j)  # Row = i, Col = j

    return None


def Sudoku():
    print_board(board)  # Before
    solve(board)
    print()
    print_board(board)  # After


Sudoku()