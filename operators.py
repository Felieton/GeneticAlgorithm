import random
import numpy as np
import chromosome as chr


def tournament_selection(population, tournament_size):
    if tournament_size > len(population):
        return None

    drawn_indexes = []
    tournament_population = []

    while len(tournament_population) != tournament_size:
        index = random.randint(0, tournament_size - 1)
        if index not in drawn_indexes:
            drawn_indexes.append(index)
            tournament_population.append(population[index])

    fittest = tournament_population[0]
    best_fitness = tournament_population[0].evaluation

    for chromosome in tournament_population:
        if chromosome.evaluation < best_fitness:
            best_fitness = chromosome.evaluation
            fittest = chromosome

    return fittest


def roulette_selection(population):
    evaluations = []
    roulette_selection_probabilities = []

    for chromosome in population:
        evaluations.append(chromosome.evaluation)

    evaluations_sum = sum(evaluations)
    inverted_probabilities_nominators = []

    for i in range(len(population)):
        inverted_probabilities_nominators.append((1 - population[i].evaluation/evaluations_sum) * evaluations_sum)

    inverted_probabilities_nominators_sum = sum(inverted_probabilities_nominators)

    for i in range(len(population)):
        roulette_selection_probabilities.append(inverted_probabilities_nominators[i] / inverted_probabilities_nominators_sum)

    print(roulette_selection_probabilities)
    chosen = np.random.choice(population, p=roulette_selection_probabilities)

    return chosen


def crossover(parents):
    child = chr.Chromosome([], [], [])
    for i in range(len(parents[0].routes_list)):
        chosen_parent = random.randint(0, 1)
        child.routes_list.append(parents[chosen_parent].routes_list[i])
        child.step_list.append(parents[chosen_parent].step_list[i])
        child.all_points_visited.append(parents[chosen_parent].all_points_visited[i])

    return child


def mutation(chromosome):
    path_index = random.randint(0, len(chromosome.step_list) - 1)
    step_list = chromosome.step_list[path_index]

    step_index = random.randint(0, len(step_list) - 1)
    step = step_list[step_index]

    if step[0] == 'left' or step[0] == 'right':
        mutation_direction = random.choice(['up', 'down'])

        if step_index == 0:
            step_list.insert(0, ('up', 0))
            step_index += 1
        if step_index == len(step_list) - 1:
            step_list.append(('down', 0))

        left_neighbour = step_list[step_index - 1]
        right_neighbour = step_list[step_index + 1]

        if mutation_direction == 'up':
            if left_neighbour[0] == 'up' and right_neighbour[0] == 'down':
                step_list[step_index - 1] = ('up', left_neighbour[1] + 1)
                step_list[step_index + 1] = ('down', right_neighbour[1] + 1)
            elif left_neighbour[0] == 'up' and right_neighbour[0] == 'up':
                step_list[step_index - 1] = ('up', left_neighbour[1] + 1)
                step_list[step_index + 1] = ('up', right_neighbour[1] - 1)
            elif left_neighbour[0] == 'down' and right_neighbour[0] == 'down':
                step_list[step_index - 1] = ('down', left_neighbour[1] - 1)
                step_list[step_index + 1] = ('down', right_neighbour[1] + 1)
            elif left_neighbour[0] == 'down' and right_neighbour[0] == 'up':
                step_list[step_index - 1] = ('down', left_neighbour[1] - 1)
                step_list[step_index + 1] = ('up', right_neighbour[1] - 1)

        elif mutation_direction == 'down':
            if left_neighbour[0] == 'up' and right_neighbour[0] == 'down':
                step_list[step_index - 1] = ('up', left_neighbour[1] - 1)
                step_list[step_index + 1] = ('down', right_neighbour[1] - 1)
            elif left_neighbour[0] == 'up' and right_neighbour[0] == 'up':
                step_list[step_index - 1] = ('up', left_neighbour[1] - 1)
                step_list[step_index + 1] = ('up', right_neighbour[1] + 1)
            elif left_neighbour[0] == 'down' and right_neighbour[0] == 'down':
                step_list[step_index - 1] = ('down', left_neighbour[1] - 1)
                step_list[step_index + 1] = ('down', right_neighbour[1] + 1)
            elif left_neighbour[0] == 'down' and right_neighbour[0] == 'up':
                step_list[step_index - 1] = ('down', left_neighbour[1] + 1)
                step_list[step_index + 1] = ('up', right_neighbour[1] + 1)

    if step[0] == 'up' or step[0] == 'down':
        mutation_direction = random.choice(['right', 'left'])

        if step_index == 0:
            step_list.insert(0, ('right', 0))
            step_index += 1
        if step_index == len(step_list) - 1:
            step_list.append(('left', 0))

        left_neighbour = step_list[step_index - 1]
        right_neighbour = step_list[step_index + 1]

        if mutation_direction == 'right':
            if left_neighbour[0] == 'right' and right_neighbour[0] == 'left':
                step_list[step_index - 1] = ('right', left_neighbour[1] + 1)
                step_list[step_index + 1] = ('left', right_neighbour[1] + 1)
            elif left_neighbour[0] == 'right' and right_neighbour[0] == 'right':
                step_list[step_index - 1] = ('right', left_neighbour[1] + 1)
                step_list[step_index + 1] = ('right', right_neighbour[1] - 1)
            elif left_neighbour[0] == 'left' and right_neighbour[0] == 'left':
                step_list[step_index - 1] = ('left', left_neighbour[1] - 1)
                step_list[step_index + 1] = ('left', right_neighbour[1] + 1)
            elif left_neighbour[0] == 'left' and right_neighbour[0] == 'right':
                step_list[step_index - 1] = ('left', left_neighbour[1] - 1)
                step_list[step_index + 1] = ('right', right_neighbour[1] - 1)

        elif mutation_direction == 'left':
            if left_neighbour[0] == 'right' and right_neighbour[0] == 'left':
                step_list[step_index - 1] = ('right', left_neighbour[1] - 1)
                step_list[step_index + 1] = ('left', right_neighbour[1] - 1)
            elif left_neighbour[0] == 'right' and right_neighbour[0] == 'right':
                step_list[step_index - 1] = ('right', left_neighbour[1] - 1)
                step_list[step_index + 1] = ('right', right_neighbour[1] + 1)
            elif left_neighbour[0] == 'left' and right_neighbour[0] == 'left':
                step_list[step_index - 1] = ('left', left_neighbour[1] - 1)
                step_list[step_index + 1] = ('left', right_neighbour[1] + 1)
            elif left_neighbour[0] == 'left' and right_neighbour[0] == 'right':
                step_list[step_index - 1] = ('left', left_neighbour[1] + 1)
                step_list[step_index + 1] = ('right', right_neighbour[1] + 1)

    fix_negative_values(chromosome, path_index)
    delete_steps_with_0(chromosome, path_index)
    concatenate_same_directions(chromosome, path_index)
    # redefine_routes_and_apv_list(chromosome, path_index)


def fix_negative_values(chromosome, path_index):
    for i in range(len(chromosome.step_list[path_index])):
        if chromosome.step_list[path_index][i][1] == -1:
            direction = chromosome.step_list[path_index][i][0]
            if direction == 'up':
                chromosome.step_list[path_index][i] = ('down', 1)
            if direction == 'down':
                chromosome.step_list[path_index][i] = ('up', 1)
            if direction == 'left':
                chromosome.step_list[path_index][i] = ('right', 1)
            if direction == 'right':
                chromosome.step_list[path_index][i] = ('left', 1)


def delete_steps_with_0(chromosome, path_index):
    new_list = []
    for i in range(len(chromosome.step_list[path_index])):
        if chromosome.step_list[path_index][i][1] != 0:
            new_list.append(chromosome.step_list[path_index][i])

    chromosome.step_list[path_index] = new_list


def concatenate_same_directions(chromosome, path_index):
    indexes_to_delete = []
    new_list = []
    for i in range(len(chromosome.step_list[path_index]) - 1):
        if chromosome.step_list[path_index][i][0] == chromosome.step_list[path_index][i + 1][0]:
            indexes_to_delete.append(i + 1)
            direction = chromosome.step_list[path_index][i][0]
            act_step_length = chromosome.step_list[path_index][i][1]
            next_step_length = chromosome.step_list[path_index][i + 1][1]
            chromosome.step_list[path_index][i] = (direction, act_step_length + next_step_length)

    for i in range(len(chromosome.step_list[path_index])):
        if i not in indexes_to_delete:
            new_list.append(chromosome.step_list[path_index][i])

    chromosome.step_list[path_index] = new_list


def redefine_routes_and_apv_list(chromosome, path_index):
    start_x = chromosome.routes_list[path_index][0].x
    start_y = chromosome.routes_list[path_index][0].y
