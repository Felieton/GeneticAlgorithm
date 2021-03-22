import sys

from src import population_generator as pg


def random_method(board, population_size):
    population = pg.generate_population(population_size, board)
    best_chromosome = get_best_chromosome(population)
    best_evaluation = get_best_fitness(population)
    worst_evaluation = get_worst_fitness(population)
    average_fitness = get_avg_fitness(population)

    return best_chromosome, (best_evaluation, worst_evaluation, average_fitness)


def get_avg_fitness(population):
    fitness_sum = 0

    for chromosome in population:
        fitness_sum += chromosome.evaluation

    return fitness_sum / len(population)


def get_best_fitness(population):
    best_fitness = sys.maxsize

    for chromosome in population:
        if chromosome.evaluation < best_fitness:
            best_fitness = chromosome.evaluation

    return best_fitness


def get_worst_fitness(population):
    worst_fitness = 0

    for chromosome in population:
        if chromosome.evaluation > worst_fitness:
            worst_fitness = chromosome.evaluation

    return worst_fitness


def get_best_chromosome(population):
    best_chromosome = None

    if population:
        best_chromosome = population[0]

    if len(population) > 1:
        for i in range(1, len(population)):
            if population[i].evaluation < best_chromosome.evaluation:
                best_chromosome = population[i]

    return best_chromosome