import exercise_loading as el
import pcb as pcb
import chromosome as chr
import chromosome_maker as chmr
import population_generator as pg
import operators as op


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
    chromosomes = [chr.Chromosome([], [[('left', 3), ('up', 2), ('right', 1)]], []),
                   chr.Chromosome([], [[('left', 5), ('up', 4), ('left', 3), ('down', 1)]], []),
                   chr.Chromosome([], [[('right', 1), ('up', 2), ('right', 1), ('up', 1)]], []),
                   chr.Chromosome([], [[('down', 1), ('right', 3), ('up', 1)]], [])]

    print("\nMutations:")
    for chromosome in chromosomes:
        print("\nbefore mutation:")
        print(chromosome.step_list)
        print("")
        op.mutation(chromosome)
        print("after mutation:")
        print(chromosome.step_list)


if __name__ == '__main__':
    width, height, list_of_connections = el.load_exercise("zad0.txt")
    board = pcb.PCB(width, height, list_of_connections)
    test_selection_operators(board)
    test_crossover(board)
    test_mutation()


