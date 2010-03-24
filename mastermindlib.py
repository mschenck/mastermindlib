"""
Library for 'MasterMind' game logic

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import random

def generate_code(challenge=2):
    piece_count = 4
    piece_options = 6

    if challenge == 1:
        piece_count = 3
    if challenge == 2:
        piece_count = 4
    elif challenge == 3:
        piece_count = 5
        piece_options = 8

    random.seed()
    pieces = range(piece_options)
    solution = []

    for iter in range(piece_count):
        piece_location = random.randint( 0, (piece_options - 1) - iter )
        solution.append( int(pieces.pop(piece_location)) )

    return solution


def check_guess(solution,input):
    """Check the user input against the passed solution
        args( solution, input )
        returns ( correct locations, correct pieces )	
    """
    uniques = set(input)
    correct_pieces = 0
    correct_locations = 0

    for piece in uniques:
        if int(piece) in solution:
            correct_pieces += 1

    for location,piece in enumerate(input):
        if int(piece) == solution[location]:
            correct_locations += 1

    return correct_locations,correct_pieces


