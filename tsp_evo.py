import random
position = [(1,4),(2,9),(7,7),(2,4),(3,5),(6,3),(9,2),(7,4)]
def sample():
    list = []
    while (len(list) != 8):
        candidate = random.randint(0,7)
        #print(candidate)
        if candidate not in list:
            list.append(candidate)
    return list
            #print(list)

def d(start_point,end_point):
    x_square = (position[start_point][0]-position[end_point][0])**2
    y_square = (position[start_point][1]-position[end_point][1])**2
    distance = (x_square + y_square)** 0.5
    return distance

class Individual:

    def __init__(self,chromosome = None):
        if chromosome is None:
            chromosome = sample()
            #print("we walked to sample "+chromosome)
        self.chromosome = chromosome

    def compute_fitness(self):
        fitness = d(self.chromosome[7],self.chromosome[0])
        for i in range(0,7):
            fitness += d(self.chromosome[i], self.chromosome[i+1])
        return fitness

    def recombine(self, other):
        crossover_point = int(random.random() * 6 + 1)
        new_chromosome = self.chromosome[0:crossover_point]
        for gene in other.chromosome:
            if not gene in new_chrmosome:
                new_chromosome.append(gene)
        return Individual(new_chromosome)

    def mutate(self):
        new_chromosome = []
        for element in self.chromosome:
            new_chromosome.append(element)
        random1 = int (random.random()*7)
        random2 = int (random.random()*7)
        while random1 == random2:
            random2 = int (random.random()*7)
        reserve = new_chromosome[random2]
        new_chromosome[random2] = new_chromosome[random1]
        new_chromosome[random1] = reserve
        return Indivual(new_chromosome)


'''class Population:
    def __init__(self,initial_size):
        self.initial_size = initial_size
        self.individuals = [Individual() for _ in range(0,initial_size)]
        self.individuals.sort(key=lambda individual: individual.compute_fitness())
        print(self.individuals)

    def evolve(self):
        self.mutate()
        self.individuals.sort(key=lambda individual: individual.compute_fitness())
        self.recombine()
        self.individuals.sort(key=lambda individual: individual.compute_fitness())
        self.individuals = self.individuals[0:self.initial_size]

    def mutate(self):
        for i in range(0, len(self.individuals)):
            self.individuals[i] = self.individuals[i].mutate()

    def recombine(self):
        pass'''
