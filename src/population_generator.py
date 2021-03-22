from src import chromosome_maker as chm


def generate_population(size, board):
    population = []
    for i in range(size):
        chromosome = chm.make_random_chromosome(board)
        chromosome.evaluate(board)
        population.append(chromosome)
    return population
