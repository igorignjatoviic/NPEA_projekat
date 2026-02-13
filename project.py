import random, math

# selection
def generateInitialPopulation(citiesSize, populationSize):
    population = []
    for _ in range(populationSize):
        route = list(range(1, citiesSize+1))
        random.shuffle(route)
        population.append(route)

    return population

def totalDistance(route, cities):
    distance = 0
    print(route)
    for i in range(len(route)):
        stCity = cities[route[i]]
        ndCity = cities[route[(i+1) % len(route)]]
        distance += math.sqrt((stCity[0] - ndCity[0])**2 + (stCity[1] - ndCity[1])**2)
    
    return distance

def loadCities(filename):
    cities = {}
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(' ')
            cities[int(line[0])] = (float(line[1]), float(line[2]))    

    return cities

if __name__ == "__main__":
    cities = loadCities("resources/data_tsp.txt")
    population = generateInitialPopulation(len(cities), 100)
    for route in population:
        print(totalDistance(route, cities))