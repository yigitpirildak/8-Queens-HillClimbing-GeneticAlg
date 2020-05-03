import numpy
import random
import time

POSITION_EMPTY = 0
POSITION_QUEEN = 1

class Board:

    def __init__(self,row,col):
        self.rows = row
        self.cols = col
        self.__initBoard()

    # Add a new queen at a random position
    def addRandomQueen(self):
        while True:
            x = random.randrange(0,self.rows)
            y = random.randrange(0,self.cols)
            if self.__isPositionEmpty(x,y):
                self.board[x][y] = POSITION_QUEEN
                break
        self.queenCount += 1
        self.queenPositions.append((x,y))
        self.score = self.evaluateBoard()

    # Add 8 new queens
    def add8Queens(self):
        for i in range(0,8):
            self.addRandomQueen()

    def __initBoard(self):
            self.board = numpy.zeros((self.rows,self.cols))
            self.queenCount = 0
            self.queenPositions = []
            self.score = 0
            self.goal = 0

    # Check if the given position is empty
    def __isPositionEmpty(self,x,y):
        if self.board[x][y] == POSITION_EMPTY:
            return True
        else:
            return False

    # Reset the board and generate an initial state
    def randomRestart(self):
        self.__initBoard()
        self.add8Queens()

    # Draw the board
    def drawBoard(self):
        for i in range(self.rows):
            for k in range(self.cols):
                if self.board[i,k] == POSITION_EMPTY:
                    print("[ ]",end="")
                elif self.board[i,k] == POSITION_QUEEN:
                    print("[W]",end="")
            print("") # Newline
        print("") # Newline

    def moveQueen(self,queen,newX,newY):
        if self.__isPositionEmpty(newX,newY):
            queenPosition = self.queenPositions[queen]
            self.board[queenPosition[0],queenPosition[1]] = POSITION_EMPTY
            self.board[newX,newY] = POSITION_QUEEN
            self.queenPositions[queen] = (newX,newY)


    def evaluateBoard(self):
        currentScore = 0
        for queen in range(0,self.queenCount):
            queenX = self.queenPositions[queen][0]
            queenY = self.queenPositions[queen][1]
            eval1 = self.__horizontalEvaluation(queen,queenX)
            eval2 = self.__verticalEvaluation(queen,queenY)
            eval3 = self.__diagonalEvaluation(queen,queenX,queenY)
            currentScore += eval1 + eval2 + eval3
        return currentScore

    def __horizontalEvaluation(self,queen,x):
        count = 0
        for i in range(0,self.queenCount):
            if i == queen:
                continue
            elif self.queenPositions[i][0] == x:
                count += 1
        return count

    def __verticalEvaluation(self,queen,y):
        count = 0
        for i in range(0,self.queenCount):
            if i == queen:
                continue
            elif self.queenPositions[i][1] == y:
                count += 1
        return count

    def __diagonalEvaluation(self,queen,x,y):
        count = 0
        for i in range(0,self.queenCount):
            if i == queen:
                continue
            else:
                queenX = self.queenPositions[i][0]
                queenY = self.queenPositions[i][1]
                if abs(x - queenX) == abs(y - queenY):
                    count += 1
        return count

    def solveWithHillClimbing(self):
        startTime = time.clock()
        randomRestartCount = 0
        moveCount = 0
        stuck = 0
        while True:
            moveFound = None
            newScore = self.score
            for queen in range(0,self.queenCount):
                oldPosition = self.queenPositions[queen] # Queen's current position
                for k in range(0,self.rows):
                    self.moveQueen(queen,k,oldPosition[1])
                    evaluation = self.evaluateBoard()
                    if (evaluation < newScore):
                        moveFound = (queen,k,oldPosition[1])
                        newScore = evaluation
                    self.moveQueen(queen,oldPosition[0],oldPosition[1])
                for k in range(0,self.cols):
                    self.moveQueen(queen,oldPosition[0],k)
                    evaluation = self.evaluateBoard()
                    if (evaluation < newScore):
                        moveFound = (queen,oldPosition[0],k)
                        newScore = evaluation
                    self.moveQueen(queen,oldPosition[0],oldPosition[1])

            if moveFound == None:
                self.randomRestart()
                randomRestartCount += 1
            else:
                self.score = newScore
                self.moveQueen(moveFound[0],moveFound[1],moveFound[2])
                moveCount += 1
                if self.score == self.goal:
                    endTime = time.clock()
                    elapsed = endTime - startTime
                    self.drawBoard()
                    return (moveCount,randomRestartCount,elapsed)
