import random

def fitness(x):
    return x*x

population = [random.randint(-10,10) for _ in range(10)]

for gen in range(20):
    population.sort(key=fitness)
    population = population[:5]
    while len(population) < 10:
        a, b = random.sample(population, 2)
        child = (a + b)//2
        if random.random() < 0.1:
            child += random.randint(-1,1)
        population.append(child)

print("Best solution:", population[0])
