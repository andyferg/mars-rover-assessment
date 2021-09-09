import string
import random

from model.plateau import Plateau
from model.rover import Rover


def run_manually():
    scope = str(input('Plateau: ')).split(' ')

    plateau = Plateau(int(scope[0]), int(scope[1]))

    choice = True

    while choice:
        landing = str(input('Rover Landing: ') or True).split(' ')
        instructions = input('Rover Instructions: ')

        rover = Rover(f'rover_{random.choice(string.ascii_letters)}', int(landing[0]), int(landing[1]), landing[2])
        plateau.add_rover(rover, instructions)

        choice = str(input('Press S to stop adding rovers. ') or True)
        choice = choice not in 'Ss'

    return plateau


def run_from_file():
    filename = input('Filename: ')

    with open(filename) as file:
        line = file.readline().strip('\n').split(':')[1]

        scope = str(line).split(' ')
        plateau = Plateau(int(scope[0]), int(scope[1]))

        while line:
            line = file.readline()

            if line:
                landing = str(line.strip('\n').split(':')[1]).split(' ')

                line = file.readline().strip('\n').split(':')[1]
                instructions = line

                rover = Rover(f'rover_{random.choice(string.ascii_letters)}', int(landing[0]), int(landing[1]), landing[2])
                plateau.add_rover(rover, instructions)

        return plateau


def results(plateau):
    for rover in plateau.rovers:
        print(f'Rover {rover.name}: {rover.coord_x} {rover.coord_y} {rover.orientation}')


def start():
    choice = True

    while choice:
        print('Press M to enter data manually, F to load from file or E to exit.')

        choice = str(input() or True)

        if choice in 'mM':
            results(run_manually())
        elif choice in 'fF':
            results(run_from_file())
        elif choice in 'eE':
            choice = False
            print('\n Exit')
        else:
            print('\n Not Valid Choice')


if __name__ == '__main__':
    start()
