import numpy as np
import sys

board = np.zeros((4, 4))

board[1][1] = -1
board[1][2] = 1
board[2][1] = 1
board[2][2] = -1


def alphaBeta(board, alpha, beta, mod, depth, parent, depthList, numList, parentList, boardList,alphaList,betaList):
    boardList.append(board)
    depthList.append(depth)
    nextPrent = numList[len(numList) - 1] + 1
    numList.append(numList[len(numList) - 1] + 1)
    parentList.append(parent)
    alphaList.append(alpha)
    betaList.append(beta)
    index=len(alphaList)-1

    if endGame(board):
        list = [countScore(board, 1), None]
        return list
    if mod:
        moves = possibleMove(board, 1)
        bestVal = [-200, None]
        if len(moves) == 0:
            testBoard = np.zeros((4, 4))
            copyBoard(board, testBoard)
            value = alphaBeta(testBoard, alpha, beta, False, depth + 1, nextPrent, depthList, numList, parentList,
                              boardList,alphaList,betaList)
            if bestVal[0] < value[0]:
                bestVal[0] = value[0]
                bestVal[1] = None
                if (bestVal[0] > alpha):
                    alpha = bestVal[0]
                    alphaList[index]= alpha
        else:
            for i in moves:
                testBoard = np.zeros((4, 4))
                copyBoard(board, testBoard)
                makeboard(testBoard, i[0], i[1], 1)
                value = alphaBeta(testBoard, alpha, beta, False, depth + 1, nextPrent, depthList, numList, parentList,
                                  boardList,alphaList,betaList)
                if bestVal[0] < value[0]:
                    bestVal[0] = value[0]
                    bestVal[1] = i

                if (bestVal[0] > alpha):
                    alpha = bestVal[0]
                    alphaList[index] = alpha
                if alpha >= beta:
                    alphaList.append(alpha)
                    betaList.append(beta)
                    boardList.append(np.zeros((4, 4)))
                    depthList.append(depth + 1)
                    numList.append(numList[len(numList) - 1] + 1)
                    parentList.append(nextPrent)
                    break
        return bestVal
    else:
        moves = possibleMove(board, -1)
        bestVal = [200, None]
        if len(moves) == 0:
            testBoard = np.zeros((4, 4))
            copyBoard(board, testBoard)
            value = alphaBeta(testBoard, alpha, beta, True, depth + 1, nextPrent, depthList, numList, parentList,
                              boardList,alphaList,betaList)
            if bestVal[0] > value[0]:
                bestVal[0] = value[0]
                bestVal[1] = None
            if (bestVal[0] < beta):
                beta = bestVal[0]
                betaList[index] = beta
        else:
            for i in moves:
                testBoard = np.zeros((4, 4))
                copyBoard(board, testBoard)
                makeboard(testBoard, i[0], i[1], -1)
                value = alphaBeta(testBoard, alpha, beta, True, depth + 1, nextPrent, depthList, numList, parentList,
                                  boardList,alphaList,betaList)
                if bestVal[0] > value[0]:
                    bestVal[0] = value[0]
                    bestVal[1] = i
                if (bestVal[0] < beta):
                    beta = bestVal[0]
                    betaList[index] = beta
                if alpha >= beta:
                    alphaList.append(alpha)
                    betaList.append(beta)
                    boardList.append(np.zeros((4, 4)))
                    depthList.append(depth + 1)
                    numList.append(numList[len(numList) - 1] + 1)
                    parentList.append(nextPrent)
                    break
        return bestVal


def copyBoard(board, testboard):
    for i in range(4):
        for j in range(4):
            testboard[i][j] = board[i][j]


def endGame(board):
    moves1 = possibleMove(board, -1)
    moves2 = possibleMove(board, 1)
    if len(moves1) == 0 and len(moves2) == 0:
        return True
    else:
        return False


def possibleMove(board, player):
    moves = []
    for i in range(4):
        for j in range(4):
            if board[i][j] != 1 and board[i][j] != -1:
                if canPlaced(board, i, j, player):
                    moves.append([i, j])
    return moves


def canPlaced(board, i, j, player):
    if i > 1 and board[i - 1][j] != player and board[i - 1][j] != 0:
        x = i - 2
        while x >= 0:
            if board[x][j] == player:
                return True
            if board[x][j] == 0:
                break
            x -= 1
    if i < 2 and board[i + 1][j] != player and board[i + 1][j] != 0:
        x = i + 2
        while x <= 3:
            if board[x][j] == player:
                return True
            if board[x][j] == 0:
                break
            x += 1
    if j > 1 and board[i][j - 1] != player and board[i][j - 1] != 0:
        x = j - 2
        while x >= 0:
            if board[i][x] == player:
                return True
            if board[i][x] == 0:
                break
            x -= 1
    if j < 2 and board[i][j + 1] != player and board[i][j + 1] != 0:
        x = j + 2
        while x <= 3:
            if board[i][x] == player:
                return True

            if board[i][x] == 0:
                break
            x += 1
    #######################################################################
    if i > 1 and j > 1 and board[i - 1][j - 1] != player and board[i - 1][j - 1] != 0:
        x = i - 2
        y = j - 2
        while x >= 0 and y >= 0:
            if board[x][y] == player:
                return True
            if board[x][y] == 0:
                break
            x -= 1
            y -= 1

    if i < 2 and j < 2 and board[i + 1][j + 1] != player and board[i + 1][j + 1] != 0:
        x = i + 2
        y = j + 2
        while x <= 3 and y <= 3:
            if board[x][y] == player:
                return True
            if board[x][y] == 0:
                break
            x += 1
            y += 1

    if i > 1 and j < 2 and board[i - 1][j + 1] != player and board[i - 1][j + 1] != 0:
        x = i - 2
        y = j + 2
        while x >= 0 and y <= 3:
            if board[x][y] == player:
                return True
            if board[x][y] == 0:
                break
            x -= 1
            y += 1

    if j > 1 and i < 2 and board[i + 1][j - 1] != player and board[i + 1][j - 1] != 0:
        x = i + 2
        y = j - 2
        while y >= 0 and x <= 3:
            if board[x][y] == player:
                return True
            if board[x][y] == 0:
                break
            x += 1
            y -= 1
    return False


def makeboard(board, i, j, player):
    # player=int(playere)
    board[i][j] = player
    if i > 1 and board[i - 1][j] != player and board[i - 1][j] != 0:
        x = i - 2
        while x >= 0:
            if board[x][j] == player:
                while x != i:
                    board[x][j] = player
                    x += 1
                break
            if board[x][j] == 0:
                break
            x -= 1
    if i < 2 and board[i + 1][j] != player and board[i + 1][j] != 0:
        x = i + 2
        while x <= 3:
            if board[x][j] == player:
                while x != i:
                    board[x][j] = player
                    x -= 1
                break
            if board[x][j] == 0:
                break
            x += 1
    if j > 1 and board[i][j - 1] != player and board[i][j - 1] != 0:
        x = j - 2
        while x >= 0:
            if board[i][x] == player:
                while x != j:
                    board[i][x] = player
                    x += 1
                break
            if board[i][x] == 0:
                break
            x -= 1
    if j < 2 and board[i][j + 1] != player and board[i][j + 1] != 0:
        x = j + 2
        while x <= 3:
            if board[i][x] == player:
                while x != j:
                    board[i][x] = player
                    x -= 1
                break
            if board[i][x] == 0:
                break
            x += 1
    #######################################################################
    if i > 1 and j > 1 and board[i - 1][j - 1] != player and board[i - 1][j - 1] != 0:
        x = i - 2
        y = j - 2
        while x >= 0 and y >= 0:
            if board[x][y] == player:
                while x != i and y != j:
                    board[x][y] = player
                    x += 1
                    y += 1
                break
            if board[x][y] == 0:
                break
            x -= 1
            y -= 1

    if i < 2 and j < 2 and board[i + 1][j + 1] != player and board[i + 1][j + 1] != 0:
        x = i + 2
        y = j + 2
        while x <= 3 and y <= 3:
            if board[x][y] == player:
                while x != i and y != j:
                    board[x][y] = player
                    x -= 1
                    y -= 1
                break
            if board[x][y] == 0:
                break
            x += 1
            y += 1

    if i > 1 and j < 2 and board[i - 1][j + 1] != player and board[i - 1][j + 1] != 0:
        x = i - 2
        y = j + 2
        while x >= 0 and y <= 3:
            if board[x][y] == player:
                while x != i and y != j:
                    board[x][y] = player
                    x += 1
                    y -= 1
                break
            if board[x][y] == 0:
                break
            x -= 1
            y += 1

    if j > 1 and i < 2 and board[i + 1][j - 1] != player and board[i + 1][j - 1] != 0:
        x = i + 2
        y = j - 2
        while y >= 0 and x <= 3:
            if board[x][y] == player:
                while x != i and y != j:
                    board[x][y] = player
                    x -= 1
                    y += 1
                break
            if board[x][y] == 0:
                break
            x += 1
            y -= 1


def countScore(board, player):
    score = 0
    for i in range(4):
        for j in range(4):
            if (board[i][j] == player):
                score += 1
    return score


def printBoard(board):
    for i in range(5):
        for j in range(5):
            if i == 0 and j == 0:
                print("-", end=" ")
            else:
                if (i == 0):
                    print(j - 1, end=" ")
                else:
                    if j == 0:
                        print(i - 1, end=" ")
                    else:
                        if board[i - 1][j - 1] == 0:
                            print("x", end=" ")
                        else:
                            if board[i - 1][j - 1] == 1:
                                print("W", end=" ")
                            else:
                                print("B", end=" ")
        print("\n", end=" ")


def showTree(depthList, parentList, boardList,alphaList,betaList):
    max = -5;
    for i in depthList:
        if (i > max):
            max = i
    for i in range(max):
        for k in range(4):
            parent = -1
            for j in range(1, len(depthList)):
                if (depthList[j] == i):
                    if parent != parentList[j]:
                        if parent!=-1:
                            print("||", end="")
                            print("\t", end="")
                        parent = parentList[j]
                    for z in range (5):
                        if(z==4):
                            print(alphaList[j],end=" ")
                            print(betaList[j],end=" ")
                        else:
                            if boardList[j][k][z]==1:
                                print("w", end=" ")
                            else:
                                if boardList[j][k][z]==-1:
                                    print("B", end=" ")
                                else:
                                    print("x",end=" ")
                    print("\t", end="")
            print("\n", end="")

        print("\n \n", end="")


def main():
    global board
    printBoard(board)
    while (not endGame(board)):
        print("please enter move number :\n")
        print("possible moves ")
        possible = possibleMove(board, -1)
        print(possible)
        print("\n")
        moveX = input("Enter x value :")
        moveY = input("Enter y value :")
        while (len(possible) != 0) and ([int(moveX), int(moveY)] not in possible):
            print("Wrong move\n")
            print("please enter move number :\n")
            print("possible moves ")
            print(possible)
            print("\n")
            moveX = input("Enter x value :")
            moveY = input("Enter y value :")
        if len(possible) != 0:
            makeboard(board, int(moveX), int(moveY), (-1))
        # printBoard(board)
        depthList = [-1]
        numList = [-1]
        parentList = [-1]
        boardList = [board]
        alphaList = [-1]
        betaList = [-1]
        nextMove = alphaBeta(board, -2000, 2000, True, 0, -1, depthList, numList, parentList, boardList,alphaList,betaList)[1]
        if leftGame(board) <= 12:
            showTree(depthList, parentList, boardList,alphaList,betaList)
        makeboard(board, nextMove[0], nextMove[1], 1)
        printBoard(board)
    pc=countScore(board,1)
    player=countScore(board,-1)
    if pc>player:
        print("PC Win : you Lose!!!!!!")
    else:
        if pc==player:
            print("Draw!!!!!!")
        else:
            print("You Win :| ")




def leftGame(board):
    num = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                num += 1
    return num


main()
