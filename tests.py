from model.plateau import Plateau
from model.rover import Rover


def start():
    ans = True
    while ans:
        print("""
        1.Add a Student
        2.Delete a Student
        3.Look Up Student Record
        4.Exit/Quit
        """)
        ans = input("What would you like to do? ")
        if ans == "1":
            print("\n Student Added")
        elif ans == "2":
            print("\n Student Deleted")
        elif ans == "3":
            print("\n Student Record Found")
        elif ans == "4":
            print("\n Goodbye")
        elif ans != "":
            print("\n Not Valid Choice Try again")



    plateau = Plateau(5, 5)

    rover_a = Rover('rover_a', 1, 2, 'N')
    rover_b = Rover('rover_b', 3, 3, 'E')

    plateau.add_rover(rover_a)
    plateau.add_rover(rover_b)

    for instruction in 'LMLMLMLMM':
        if instruction == 'M':
            possible_step = rover_a.possible_step()
            coord_x = possible_step[0]
            coord_y = possible_step[1]

            if plateau.can_move(coord_x, coord_y):
                rover_a.move(coord_x, coord_y)
        else:
            rover_a.set_orientation(instruction)

    for instruction in 'MMRMMRMRRM':
        if instruction == 'M':
            possible_step = rover_b.possible_step()
            coord_x = possible_step[0]
            coord_y = possible_step[1]

            if plateau.can_move(coord_x, coord_y):
                rover_b.move(coord_x, coord_y)
        else:
            rover_b.set_orientation(instruction)

    print(rover_a.coord_x, rover_a.coord_y, rover_a.orientation)
    print(rover_b.coord_x, rover_b.coord_y, rover_b.orientation)


if __name__ == "__main__":
    start()
