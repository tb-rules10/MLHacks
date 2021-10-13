global board
board = [[" "," "," "],[" "," "," "],[" "," "," "]]
player = "X"


def printBoard(board):
    for line in board:
        print(line)


def makeMove():
    global player
    print("Player "+player+":-")
    x = int(input("Enter X-coordinate - "))
    y = int(input("Enter Y-coordinate - "))

    while board[y][x] != " ":
        print("Choose an empty spot!")
        x = int(input("Enter X-coordinate - "))
        y = int(input("Enter Y-coordinate - "))

    if player == "X":
        board[y][x] = "X"
        player = "O"
    else:
        board[y][x] = "O"
        player = "X"

"""
Did that player just Win!
"""

def isWin():
    global player
    if player == "X":
        p = "O"
    else:
        p = "X"
    # row
    for c in range(len(board)):
        win = True
        for r in range(len(board)):
            if board[c][r] != p:
                win = False
                break
        if win:
            return True
    # column
    for c in range(len(board)):
        win = True
        for r in range(len(board)):
            if board[r][c] != p:
                win = False
                break
        if win:
            return True

    # diagonals
    win = True
    for c in range(3):
        if board[c][c] != p:
            win = False
            break
    if win:
        return True

    win = True
    for r in range(len(board)):
        if board[r][len(board)-1-r] != p:
            win = False
            break
    if win:
        return True

    return False



def main():
    gamewon = False
    while gamewon == False:
        printBoard(board)
        makeMove()
        gamewon = isWin()
    print("GAMEOVER")
    printBoard(board)

main()
