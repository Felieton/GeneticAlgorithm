import chromosome_maker as chm


def generate_population(size, board):
    population = []
    for i in range(size):
        chromosome = chm.make_random_chromosome(board)
        chromosome.evaluation = evaluate(chromosome, board)
        population.append(chromosome)
    return population


def evaluate(self, pcb):
    weights = [0.45, 0.05, 0.05, 0.2, 0.25]
    evaluation = 0
    evaluation += self.get_intersection_amount() * weights[0]
    evaluation += self.get_routes_length() * weights[1]
    evaluation += self.get_segments_amount() * weights[2]
    evaluation += self.get_routes_outside_the_board_amount(pcb) * weights[3]
    evaluation += self.get_routes_outside_the_board_length(pcb) * weights[4]
    self.evaluation = evaluation
    return evaluation
