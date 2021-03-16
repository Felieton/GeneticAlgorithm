class Chromosome:
    def __init__(self, routes_list, step_list, all_points_visited):
        self.evaluation = None
        self.routes_list = routes_list
        self.step_list = step_list
        self.all_points_visited = all_points_visited

    def print_me(self):
        for i in range(len(self.routes_list)):
            print(f"Route of connection {i + 1}:")
            print(self.step_list[i])
            for j in range(len(self.routes_list[i])):
                print(f"({self.routes_list[i][j].x}, {self.routes_list[i][j].y})", end=" ")
            print("\nall points visited:")
            for j in range(len(self.all_points_visited[i])):
                print(f"({self.all_points_visited[i][j].x}, {self.all_points_visited[i][j].y})", end=" ")
            print("\n")

    def get_intersection_amount(self):
        all_points = []
        for i in range(len(self.routes_list)):
            for j in range(len(self.all_points_visited[i])):
                all_points.append((self.all_points_visited[i][j].x, self.all_points_visited[i][j].y))
        return len(all_points) - len(set(all_points))

    def get_routes_length(self):
        length = 0
        for i in range(len(self.step_list)):
            for j in range(len(self.step_list[i])):
                length += self.step_list[i][j][1]
        return length

    def get_segments_amount(self):
        amount = 0
        for i in range(len(self.step_list)):
            amount += len(self.step_list[i])
        return amount

    def get_routes_outside_the_board_amount(self, pcb):
        amount = 0
        for i in range(len(self.routes_list)):
            last_outside = False
            for j in range(len(self.routes_list[i])):
                outside_condition = self.routes_list[i][j].x < 0 or self.routes_list[i][j].x > (pcb.width - 1) or \
                        self.routes_list[i][j].y < 0 or self.routes_list[i][j].y > (pcb.height - 1)
                if last_outside and not outside_condition:
                    amount += 1
                if outside_condition:
                    amount += 1
                    last_outside = True
                else:
                    last_outside = False
        return amount

    def get_routes_outside_the_board_length(self, pcb):
        length = 0
        for i in range(len(self.all_points_visited)):
            last_outside = False
            for j in range(len(self.all_points_visited[i])):
                outside_condition = self.all_points_visited[i][j].x < 0 or self.all_points_visited[i][j].x > (pcb.width - 1) or \
                                    self.all_points_visited[i][j].y < 0 or self.all_points_visited[i][j].y > (pcb.height - 1)
                if last_outside and not outside_condition:
                    length += 1
                if outside_condition:
                    length += 1
                    last_outside = True
                else:
                    last_outside = False
        return length

    def print_my_evaluations(self, pcb):
        print(f"intersections: {self.get_intersection_amount()}")
        print(f"routes length: {self.get_routes_length()}")
        print(f"segments: {self.get_segments_amount()}")
        print(f"routes outside the board: {self.get_routes_outside_the_board_amount(pcb)}")
        print(f"length of parts or routes outside the board: {self.get_routes_outside_the_board_length(pcb)}")
        print(f"evaluation: {self.evaluation}")
