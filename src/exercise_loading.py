from src import point as pt


def load_exercise(filename):
    opened = open(filename, "r")
    first_line = opened.readline()
    dimensions = first_line.split(';')
    width = int(dimensions[0])
    height = int(dimensions[1])
    lines = opened.readlines()
    list_of_connections = []
    for line in lines:
        list_of_elements = line.strip().split(';')
        list_of_connections.append((pt.Point(int(list_of_elements[0]), int(list_of_elements[1])),
                                    pt.Point(int(list_of_elements[2]), int(list_of_elements[3]))))

    return width, height, list_of_connections
