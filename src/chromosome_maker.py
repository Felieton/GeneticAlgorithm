from src import chromosome as chr, point as pt
import random
import math

UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4


def make_random_chromosome(pcb):

    chromosome = chr.Chromosome([], [], [])
    for i in range(len(pcb.list_of_connections)):
        chromosome.routes_list.append([])
        chromosome.step_list.append([])
        chromosome.all_points_visited.append([])
        chromosome.routes_list[i].append(pcb.list_of_connections[i][0])
        chromosome.all_points_visited[i].append(pcb.list_of_connections[i][0])
        x = chromosome.routes_list[i][0].x
        y = chromosome.routes_list[i][0].y
        random_steps_amount = random.randint(1, math.ceil((pcb.height + pcb.width)/5))

        for j in range(random_steps_amount):
            step_direction, step_length = get_rand_step(pcb.width, pcb.height)

            if chromosome.step_list[i]:
                if (step_direction == 1 or step_direction == 3) and\
                        (chromosome.step_list[i][-1][0] == 'up' or chromosome.step_list[i][-1][0] == 'down'):
                    step_direction += 1
                if (step_direction == 2 or step_direction == 4) and\
                        (chromosome.step_list[i][-1][0] == 'left' or chromosome.step_list[i][-1][0] == 'right'):
                    step_direction -= 1

            x_delta = 0
            y_delta = 0
            x_step_delta = 0
            y_step_delta = 0
            step_name = ""

            if step_direction == UP:
                y_delta = step_length
                y_step_delta = 1
                step_name = "up"
            if step_direction == DOWN:
                y_delta = -step_length
                y_step_delta = -1
                step_name = "down"
            if step_direction == RIGHT:
                x_delta = step_length
                x_step_delta = 1
                step_name = "right"
            if step_direction == LEFT:
                x_delta = -step_length
                x_step_delta = -1
                step_name = "left"

            for k in range(step_length):
                chromosome.all_points_visited[i].append(pt.Point(x + (k + 1) * x_step_delta, y + (k + 1) * y_step_delta))

            x = x + x_delta
            y = y + y_delta
            chromosome.routes_list[i].append(pt.Point(x, y))
            chromosome.step_list[i].append((step_name, step_length))

            if chromosome.routes_list[i][-1].x == pcb.list_of_connections[i][1].x and \
                    chromosome.routes_list[i][-1].y == pcb.list_of_connections[i][1].y:
                break
        connect_points(pcb, chromosome, i)

    return chromosome


def get_rand_step(width, height):
    step_direction = random.randint(1, 4)
    if step_direction == UP or step_direction == DOWN:
        step_range = math.ceil(height / 2)
    else:
        step_range = math.ceil(width / 2)

    step_length = random.randint(1, step_range)

    return step_direction, step_length


def connect_points(pcb, chromosome, i):
    current_x = chromosome.routes_list[i][-1].x
    wanted_x = pcb.list_of_connections[i][1].x
    current_y = chromosome.routes_list[i][-1].y
    wanted_y = pcb.list_of_connections[i][1].y

    if current_x == wanted_x and current_y == wanted_y:
        return

    else:
        delta_x = wanted_x - current_x
        delta_y = wanted_y - current_y

        if chromosome.step_list[i][-1][0] == 'up' or chromosome.step_list[i][-1][0] == 'down':
            connect_horizontally(current_x, current_y, delta_x, 0, chromosome, i)
            connect_vertically(current_x, current_y, delta_x, delta_y, chromosome, i)
        else:
            connect_vertically(current_x, current_y, 0, delta_y, chromosome, i)
            connect_horizontally(current_x, current_y, delta_x, delta_y, chromosome, i)


def connect_horizontally(current_x, current_y, delta_x, delta_y, chromosome, i):
    if delta_x != 0:
        chromosome.routes_list[i].append(pt.Point(current_x + delta_x, current_y + delta_y))
    if delta_x > 0:
        chromosome.step_list[i].append(('right', delta_x))
        for k in range(delta_x):
            chromosome.all_points_visited[i].append(pt.Point(current_x + (k + 1), current_y + delta_y))
    if delta_x < 0:
        chromosome.step_list[i].append(('left', -delta_x))
        for k in range(-delta_x):
            chromosome.all_points_visited[i].append(pt.Point(current_x - (k + 1), current_y + delta_y))


def connect_vertically(current_x, current_y, delta_x, delta_y, chromosome, i):
    if delta_y != 0:
        chromosome.routes_list[i].append(pt.Point(current_x + delta_x, current_y + delta_y))
    if delta_y > 0:
        chromosome.step_list[i].append(('up', delta_y))
        for k in range(delta_y):
            chromosome.all_points_visited[i].append(pt.Point(current_x + delta_x, current_y + (k + 1)))
    if delta_y < 0:
        chromosome.step_list[i].append(('down', -delta_y))
        for k in range(-delta_y):
            chromosome.all_points_visited[i].append(pt.Point(current_x + delta_x, current_y - (k + 1)))
