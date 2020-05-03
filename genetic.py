from board import Board
import random
import copy
import time

def crossOver(parent1,parent2):
    crossover_point = random.randrange(0,4)
    offspring = copy.deepcopy(parent1)
    #print("before crossover",offspring.score)
    for i in range(0,crossover_point):
        offspring.moveQueen(i,parent2.queenPositions[i][0],parent2.queenPositions[i][1])
    offspring.score = offspring.evaluateBoard()
    #print("after crossover",offspring.score)
    return (offspring)

def mutation(child):
    for i in range(0,8):
        chanceToMutate = random.randint(0,100)
        if (chanceToMutate <= 20):
            randomQueen = random.randrange(0,8)
            randomX = random.randrange(0,8)
            randomY = random.randrange(0,8)
            child.moveQueen(randomQueen,randomX,randomY)
            child.score = child.evaluateBoard()

if __name__ == '__main__':
    initialPopulationCount = 100
    population = []


    # Generate the initial population
    for i in range(0,initialPopulationCount):
        board = Board(8,8)
        board.add8Queens()
        population.append(board)

    bestParentEver = None
    startTime = time.clock()
    while True:
        bestParent = population[0]
        secondBestParent = population[1]

        if (bestParent.score > secondBestParent.score):
            tmp = bestParent
            bestParent = secondBestParent
            secondBestParent = tmp

        worstParent = population[0]

        for i in range(2,len(population)):
            if population[i].score < bestParent.score:
                secondBestParent = bestParent
                bestParent = population[i]
            elif population[i].score < secondBestParent.score:
                secondBestParent = population[i]


        if bestParent.score == 0:
            endTime = time.clock()
            elapsed = endTime - startTime
            bestParent.drawBoard()
            print("Elapsed time =",elapsed)
            break

        offspring = crossOver(bestParent,secondBestParent)
        mutation(offspring)
        population.append(offspring)

        for i in range(1,len(population)):
            if population[i].score > worstParent.score:
                worstParent = population[i]

        population.remove(worstParent)

        if (bestParentEver == None):
            bestParentEver = bestParent.score
            print("New best solution =",bestParentEver)
        elif (bestParent.score < bestParentEver):
            bestParentEver = bestParent.score
            print("New best solution =",bestParentEver)
