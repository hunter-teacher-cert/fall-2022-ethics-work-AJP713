# gol.py
# Adam Prado
# CSCI 77800 Fall 2022
# 9/5/22

import random

dead = '-'
alive = '@'
percentAlive = 50

def print_board(board2D):
   output = ''
   for i in board2D:
        for j in i:
            output = output + ' ' + j
        output = output + '\n'    
   print(output)     

def create_board(rows,cols):
    board = []
    for i in range(rows):
        temprow = []
        for j in range(cols):
            tempRand = random.randint(0, 100)
            if tempRand > percentAlive:  
                temprow.append(dead)
            else:
                temprow.append(alive)
        board.append(temprow)
    return board


def count_neighbors(board, r, c):
    numNeighs = 0
    for i in range (r-1, r+2):
        for j in range (c-1, c+2):
            if i > -1 and i < len(board) and j > -1 and j < len(board[i]) and not(r==i and c ==j):
                if board[i][j] == alive:
                    numNeighs = numNeighs + 1
    return numNeighs
    
def getNextGenCell(board,r,c):
    numN = count_neighbors(board,r,c)
    if board[r][c]== alive:
        if numN == 2 or numN == 3:
            return alive
        else:
            return dead
    else:
        if numN == 3:
            return alive
        else:
            return dead

def generateNextBoard(board):
    newBoard = []
    for i in range(len(board)):
        tempList = []
        for j in range(len(board[i])):
            tempList.append(getNextGenCell(board,i,j))
        newBoard.append(tempList)
    return newBoard


newBoard = create_board(7,7)
for i in range(10):
    print("generation: ", i ,"\n")
    boardNext = generateNextBoard(newBoard)
    print_board(boardNext)
    newBoard = boardNext
    
    