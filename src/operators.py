import math
import random
import copy as cop
from src import chromosome as chr, point as pt


def tournament_selection(population, tournament_size):
    if tournament_size > len(population):
        return None

    drawn_indexes = []
    tournament_population = []

    while len(tournament_population) != tournament_size:
        index = random.randint(0, len(population) - 1)
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

    for chromosome in population:
        evaluations.append(chromosome.evaluation)

    min_eval = min(evaluations)
    weights = []

    for chromosome in population:
        weights.append(min_eval / chromosome.evaluation)

    chosen = random.choices(population, weights)[0]

    return chosen


def crossover(parents, crossings):
    child = chr.Chromosome([], [], [])
    last = 1
    counter = 0

    for i in range(len(parents[0].routes_list)):
        chosen_parent = 0
        if crossings == 0:
            chosen_parent = random.randint(0, 1)
        elif crossings == 1:
            if i <= len(parents[0].routes_list) / 2:
                chosen_parent = 0
            else:
                chosen_parent = 1
        elif crossings < len(parents[0].routes_list):
            if counter == math.floor(len(parents[0].routes_list) / crossings):
                last *= -1
                counter = 0
            if last == 1:
                chosen_parent = 0
            else:
                chosen_parent = 1
            counter += 1

        route = cop.deepcopy(parents[chosen_parent].routes_list[i])
        steps = cop.deepcopy(parents[chosen_parent].step_list[i])
        apv = cop.deepcopy(parents[chosen_parent].all_points_visited[i])

        child.routes_list.append(route)
        child.step_list.append(steps)
        child.all_points_visited.append(apv)

    return child


def multiple_crossover(parents, num_of_parents):
    child = chr.Chromosome([], [], [])

    for i in range(len(parents[0].routes_list)):
        chosen_parent = random.randint(0, num_of_parents - 1)
        route = cop.deepcopy(parents[chosen_parent].routes_list[i])
        steps = cop.deepcopy(parents[chosen_parent].step_list[i])
        apv = cop.deepcopy(parents[chosen_parent].all_points_visited[i])

        child.routes_list.append(route)
        child.step_list.append(steps)
        child.all_points_visited.append(apv)

    return child


def mutation(chromosome, board):
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
    redefine_routes_and_apv_list(chromosome, path_index, board)


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


def redefine_routes_and_apv_list(chromosome, path_index, board):
    x = chromosome.routes_list[path_index][0].x
    y = chromosome.routes_list[path_index][0].y
    redefined_routes_list = []
    redefined_apv_list = []
    redefined_routes_list.append(chromosome.routes_list[path_index][0])
    redefined_apv_list.append(chromosome.all_points_visited[path_index][0])

    for i in range(len(chromosome.step_list[path_index])):
        step_direction = chromosome.step_list[path_index][i][0]
        step_length = chromosome.step_list[path_index][i][1]

        x_delta = 0
        y_delta = 0
        x_step_delta = 0
        y_step_delta = 0

        if step_direction == 'up':
            y_delta = step_length
            y_step_delta = 1
        if step_direction == 'down':
            y_delta = -step_length
            y_step_delta = -1
        if step_direction == 'right':
            x_delta = step_length
            x_step_delta = 1
        if step_direction == 'left':
            x_delta = -step_length
            x_step_delta = -1

        for k in range(step_length):
            redefined_apv_list.append(pt.Point(x + (k + 1) * x_step_delta, y + (k + 1) * y_step_delta))

        x = x + x_delta
        y = y + y_delta

        redefined_routes_list.append(pt.Point(x, y))

    chromosome.routes_list[path_index] = redefined_routes_list
    chromosome.all_points_visited[path_index] = redefined_apv_list
    chromosome.evaluate(board)
