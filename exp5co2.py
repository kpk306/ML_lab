import random

features = 5
population = [[random.randint(0,1) for _ in range(features)] for _ in range(6)]

def fitness(chrom):
    return sum(chrom)

for gen in range(10):
    population.sort(key=fitness, reverse=True)
    population = population[:3]
    while len(population) < 6:
        p1, p2 = random.sample(population, 2)
        cp = p1[:2] + p2[2:]
        population.append(cp)

print("Best Feature Set:", population[0])
