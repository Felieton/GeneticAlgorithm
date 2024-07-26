import sys
from src import operators as op, population_generator as pg
import random
import copy


class GeneticAlgorithm:
    def __init__(self, board, crossover_prob, mutation_prob):
        self.board = board
        self.crossover_probability = crossover_prob
        self.mutation_probability = mutation_prob

    def genetic_algorithm(self, generation_size, generation_amount, selection_type, elitist_size, multiple_parents):
        population = pg.generate_population(generation_size, self.board)

        all_generations_avg_fitness = []
        all_generations_best_fitness = []
        all_generations_worst_fitness = []

        all_generations_avg_fitness.append(get_avg_fitness(population))
        all_generations_best_fitness.append(get_best_fitness(population))
        all_generations_worst_fitness.append(get_worst_fitness(population))
        best_chromosome = get_best_chromosome(population)

        for i in range(generation_amount - 1):
            generation_population = []
            if elitist_size != 0:
                for j in range(elitist_size):
                    generation_population.append(best_chromosome)
            while len(generation_population) < generation_size:
                if selection_type == "roulette":
                    parent1 = op.roulette_selection(population)
                    parent2 = op.roulette_selection(population)
                    if multiple_parents:
                        parent3 = op.roulette_selection(population)
                        parent4 = op.roulette_selection(population)
                else:
                    parent1 = op.tournament_selection(population, 10)
                    parent2 = op.tournament_selection(population, 10)

                if multiple_parents:
                    if random.random() < self.crossover_probability:
                        child = op.multiple_crossover([parent1, parent2, parent3, parent4], 4)
                    else:
                        child = copy.deepcopy(parent1)
                else:
                    if random.random() < self.crossover_probability:
                        child = op.crossover([parent1, parent2], 0)
                    else:
                        child = copy.deepcopy(parent1)
                if random.random() < self.mutation_probability:
                    op.mutation(child, self.board)

                child.evaluate(self.board)
                generation_population.append(child)

                if child.evaluation < best_chromosome.evaluation:
                    best_chromosome = copy.deepcopy(child)

            all_generations_avg_fitness.append(get_avg_fitness(generation_population))
            all_generations_best_fitness.append(get_best_fitness(generation_population))
            all_generations_worst_fitness.append(get_worst_fitness(generation_population))
            population = copy.deepcopy(generation_population)

        return best_chromosome, (all_generations_avg_fitness, all_generations_best_fitness, all_generations_worst_fitness)


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
