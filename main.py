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
        self.geneticAlgorithm()
    
    def geneticAlgorithm(self):
        nextPopulation = []
        solution = False
        for i in range(len(self.population)-1):
            parent1, parent2 = self.population[i], self.population[i+1]
            child = self.reproduce(parent1, parent2)
            if self.mutation > random.random():
                child = self.mutate(child)
            self.counter += 1
            print(child, self.counter)
            nextPopulation.append(child)
        self.population = nextPopulation
        for individual in self.population:
            if self.fitness(individual) == 28:
                solution = individual.tolist()
                print('Solution found')
                print(solution)
                break
        else:
            self.iterations -= 1
            if self.iterations == 0:
                print('No solution')
                return False
            self.geneticAlgorithm()
        return solution

    def mutate(self, child):
        genMutate = random.randint(0, len(child)-1)
        child[genMutate] = random.randint(0, self.size-1)
        return child

    def reproduce(self, parent1, parent2):
        crossover = random.randint(1, self.size-1)
        return (np.concatenate((np.array(parent1[0:crossover]), np.array(parent2[crossover:self.size]))))
    
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
        return 28 - conflicts

if __name__ == '__main__':
    size = 8
    iteration = 600
    popSize = 250
    mutation = 0.85
    ans = NQuenne(size, iteration, popSize, mutation)
    print(ans)