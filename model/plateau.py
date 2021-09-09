class Plateau:
    rovers = []

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def can_move(self, coord_x, coord_y):
        return 0 <= coord_x <= self.rows and 0 <= coord_y <= self.columns

    def add_rover(self, rover, instructions):
        for instruction in instructions:
            if instruction == 'M':
                possible_step = rover.possible_step()
                coord_x = possible_step[0]
                coord_y = possible_step[1]

                if self.can_move(coord_x, coord_y):
                    rover.move(coord_x, coord_y)
            else:
                rover.set_orientation(instruction)

        self.rovers.append(rover)

    def get_rover(self, name):
        rover = None

        for item in self.rovers:
            if item.name == name:
                rover = item
                break

        return rover
