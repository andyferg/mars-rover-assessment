class Rover:
    def __init__(self, name, coord_x, coord_y, orientation):
        self.name = name
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.orientation = orientation

    def move(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def possible_step(self):
        STEPS = dict(
            N=[self.coord_x, self.coord_y + 1],
            S=[self.coord_x, self.coord_y - 1],
            E=[self.coord_x + 1, self.coord_y],
            W=[self.coord_x - 1, self.coord_y],
        )
        return STEPS[self.orientation]

    def set_orientation(self, instruction):
        OPTIONS = dict(
            NR='E', NL='W',
            SR='W', SL='E',
            ER='S', EL='N',
            WR='N', WL='S'
        )
        self.orientation = OPTIONS[f'{self.orientation}{instruction}']
