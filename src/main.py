from src import chromosome as chr, chromosome_maker as chmr, exercise_loading as el, genetic_algorithm as ga, \
    operators as op, pcb as pcb, plot_data as plot, population_generator as pg, random_method as rm,\
    simulated_annealing as sa


def test_selection_operators(board):
    population = pg.generate_population(5, board)
    print("Small population evaluations:")
    for chromosome in population:
        print(chromosome.evaluation, end=", ")

    print("\n\nSelected by tournament selection: ")
    fittest_tournament: chr.Chromosome = op.tournament_selection(population, 5)
    print(fittest_tournament.evaluation)

    print("\nProbabilities of being chosen:")
    fittest_roulette: chr.Chromosome = op.roulette_selection(population)
    print("chosen evaluation:")
    print(fittest_roulette.evaluation)


def test_crossover(board):
    parents = [chmr.make_random_chromosome(board), chmr.make_random_chromosome(board)]
    print("\nparent 1:")

    for list in parents[0].step_list:
        print(list)

    print("parent 2:")

    for list in parents[1].step_list:
        print(list)

    child = op.crossover(parents)

    print("child:")
    for list in child.step_list:
        print(list)


def test_mutation():
    chromosomes = pg.generate_population(5, board)

    print("\nMutations:")
    for chromosome in chromosomes:
        print("\nbefore mutation:")
        print(chromosome.step_list)
        print("")
        op.mutation(chromosome, board)
        print("after mutation:")
        print(chromosome.step_list)


def test_genetic_alg():
    cross_prob = 0.6
    mutation_prob = 0.6
    gen_size = 100
    gen_amount = 100
    multiple_parents = False

    best_chromosome, (avg_fitness, best_fitness, worst_fitness) =\
        ga.GeneticAlgorithm(board, cross_prob, mutation_prob).genetic_algorithm(gen_size, gen_amount, "roulette", 0, multiple_parents)

    print(min(best_fitness))
    print(max(worst_fitness))
    print(sum(avg_fitness) / len(avg_fitness))

    plot.plot_data_on_chart(avg_fitness, best_fitness, worst_fitness)


def test_simulated_annealing():
    temperature = 5000
    for i in range(1, 11):
        all = 0
        best = 1000
        worst = 0
        for j in range(10):
            res = sa.SimulatedAnnealing(board).simulated_annealing(temperature, i)
            all += res
            if res > worst:
                worst = res
            if res < best:
                best = res
        print(f'for {i}: avg: {all/10}    best: {best}    worst: {worst}')


def test_random_method():
    best_chromosome, (best_fitness, worst_fitness, avg_fitness) = rm.random_method(board, 25000)
    print(best_fitness)
    print(worst_fitness)
    print(avg_fitness)


if __name__ == '__main__':
    width, height, list_of_connections = el.load_exercise("../exercises/zad1.txt")
    board = pcb.PCB(width, height, list_of_connections)
    # test_genetic_alg()
    test_simulated_annealing()
