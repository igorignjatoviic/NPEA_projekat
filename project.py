import random, math


def generateGenerations(numGenerations, cities):    # generates generations and chooses the best solution for each
    population = generateInitialPopulation(len(cities))
    for i in range(numGenerations):
        population = generateNewPopulation(cities, population)

        distances = [totalDistance(route, cities) for route in population]
        bestDistance = min(distances)
        bestRoute = population[distances.index(bestDistance)]

        print(f"Generation {i + 1}: ", end="")
        for city in bestRoute:
            print(f"{city} -> ", end="")
        print(bestRoute[0])
        print(f"Distance: {bestDistance:.2f}")
        print()

        
def generateNewPopulation(cities, population):      # generates new population based on the old one
    newPopulation = []
    newPopulation.append(elitis(cities, population))

    while len(newPopulation) < len(population):
        stParent = tournamentSelection(cities, population)
        ndParent = tournamentSelection(cities, population)
        child = orderCrossover(stParent, ndParent)
        child = swapMutation(child)
        newPopulation.append(child)
    
    return newPopulation


def generateInitialPopulation(citiesSize, populationSize=100):      # generates first population
    population = []
    for _ in range(populationSize):
        route = list(range(1, citiesSize+1))
        random.shuffle(route)
        population.append(route)

    return population


def totalDistance(route, cities):       # calculates Euclidean distance
    distance = 0
    for i in range(len(route)):
        stCity = cities[route[i]]
        ndCity = cities[route[(i+1) % len(route)]]  # goes back to the starting city (with index 0) when it reaches the last index
        distance += math.sqrt((stCity[0] - ndCity[0])**2 + (stCity[1] - ndCity[1])**2)
    
    return distance


def tournamentSelection(cities, population, chromosomes=10):     # tournament selection method
    selected = random.sample(population, chromosomes)
    return elitis(cities, selected)


def orderCrossover(stParent, ndParent):     # crossover method that takes interval of first parent, second parent is filling him up
    child = [None] * len(stParent)
    start, end = sorted(random.sample(range(len(stParent)+1), 2))
    child[start:end] = stParent[start:end]
    
    ndParentIdx = 0
    for i in range(len(child)):
        if child[i] is None:
            while ndParent[ndParentIdx] in child:
                ndParentIdx += 1
            child[i] = ndParent[ndParentIdx]
    
    return child


def swapMutation(route, mutationRate=0.2):      # swap mutation method, permutation of list if conditions are met
    newRoute = route.copy()
    if random.random() < mutationRate:
        i, j = random.sample(range(len(newRoute)), 2)
        newRoute[i], newRoute[j] = newRoute[j], newRoute[i]

    return newRoute


def elitis(cities, population):     # returns first best route
    best = min(population, key=lambda route: totalDistance(route, cities))
    return best


def loadCities(filename):   # loads cities from .txt into dict
    cities = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(' ')
            cities[int(line[0])] = (float(line[1]), float(line[2]))    

    return cities


if __name__ == "__main__":
    cities = loadCities("resources/data_tsp.txt")
    generateGenerations(5, cities)