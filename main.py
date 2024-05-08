import random
import numpy as np

class NQuenne:
    def __init__(self, size, iterations, popSize, mutation) -> None:
        self.size = size
        self.iterations = iterations
        self.popSize = popSize
        self.mutation = mutation
        self.counter = 0
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.population = []
        for _ in range(popSize):
            self.population.append(np.random.random_integers(low=0, high=self.size-1, size=self.size))
        #print(self.population)
    
    def geneticAlgorithm(self):
        while self.iterations:
            nextPopulation = []
            solution = None
            for i in range(len(self.population)-1):
                parent1, parent2 = self.population[i], self.population[i+1]
                childs = self.reproduce(parent1, parent2)
                for child in childs:
                    if self.mutation > random.random():
                        child = self.mutate(child)
                    self.counter += 1
                    print(child, self.counter, 'fitnes - ', self.fitness(child))
                    nextPopulation.append(child)
            self.population = nextPopulation
            best_board = min(self.population, key=self.fitness)
            if self.fitness(best_board) == 0:
                solution = best_board
                return solution
            self.iterations -= 1
        return solution

    def mutate(self, child):
        genMutate = random.randint(0, len(child)-1)
        child[genMutate] = random.randint(0, self.size-1)
        return child

    def reproduce(self, parent1, parent2):
        crossover = random.randint(1, self.size-1)
        return (np.concatenate((
            np.array(parent1[0:crossover]), 
            np.array(parent2[crossover:self.size])
            )), np.concatenate((
            np.array(parent2[0:crossover]), 
            np.array(parent1[crossover:self.size])
            )))
    
    def fitness(self, individual):
        # row = 0
        # currentBoard = self.board
        # for column in individual:
        #     currentBoard[row][column] = 1
        #     row += 1
        conflicts = 0
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if individual[i] == individual[j] or abs(individual[i] - individual[j]) == j - i:
                    conflicts += 1
        return conflicts

if __name__ == '__main__':
    size = 10
    iteration = 1000
    popSize = 300
    mutation = 0.35
    ans = NQuenne(size, iteration, popSize, mutation)
    result = ans.geneticAlgorithm()
    print(result, f'its answer for n queen, n = {size}')