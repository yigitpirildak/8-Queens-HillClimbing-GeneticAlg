from board import Board

if __name__ == '__main__':
    numberOfGames = 25
    board = Board(8,8)
    board.add8Queens()
    listOfStats = []
    for i in range(0,numberOfGames):
        moveCount,randomRestartCount,elapsed = board.solveWithHillClimbing()
        listOfStats.append((moveCount,randomRestartCount,elapsed))
        print("Moves =",moveCount,"Random Restart =",randomRestartCount,"Time spent =",elapsed)

    sumOfMoves = 0
    sumOfRestart = 0
    sumOfElapsed = 0
    for i in listOfStats:
        sumOfMoves += i[0]
        sumOfRestart += i[1]
        sumOfElapsed += i[2]

    print("Average Moves =",sumOfMoves/numberOfGames,
          "\nAverage Random Restart =",sumOfRestart/numberOfGames,
          "\nAverage Time spent =",sumOfElapsed/numberOfGames)
