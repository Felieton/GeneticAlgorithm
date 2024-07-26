import sys
from src import operators as op, population_generator as pg
import random
import copy


class SimulatedAnnealing:
    def __init__(self, board):
        self.board = board

    def simulated_annealing(self, temperature, mult):
        individual = pg.generate_population(1, self.board)[0]
        for i in range(temperature):
            current_energy = individual.evaluation
            # print(current_energy)
            old_individual = copy.deepcopy(individual)
            op.mutation(individual, self.board)
            next_energy = individual.evaluation
            delta_energy = next_energy - current_energy
            #print(delta_energy)
            if delta_energy > 0:
                if abs(delta_energy)*mult/temperature < random.random():
                    individual = old_individual
        return individual.evaluation
