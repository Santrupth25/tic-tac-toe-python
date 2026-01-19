def checkSum(a, b, c):
    return a + b + c

def printBoard(xState, zState):
    board = []
    for i in range(9):
        if xState[i]:
            board.append('X')
        elif zState[i]:
            board.append('O')
        else:
            board.append(str(i))

    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def checkWin(xState, zState):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for win in wins:
        if checkSum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("X won the match 🎉")
            return 1
        if checkSum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("O won the match 🎉")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0]*9
    zState = [0]*9
    turn = 1  # 1 for X, 0 for O

    print("Welcome to Tic Tac Toe")

    while True:
        printBoard(xState, zState)

        try:
            value = int(input("Enter position (0-8): "))
            if value < 0 or value > 8:
                print("Invalid position. Choose 0-8.")
                continue
            if xState[value] or zState[value]:
                print("Position already taken.")
                continue
        except ValueError:
            print("Enter a number only.")
            continue

        if turn == 1:
            xState[value] = 1
        else:
            zState[value] = 1

        cwin = checkWin(xState, zState)
        if cwin != -1:
            print("Match Over")
            break

        if sum(xState) + sum(zState) == 9:
            print("It's a Draw")
            break

        turn = 1 - turn
