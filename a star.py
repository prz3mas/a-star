import sys
from math import sqrt

class Square:
    def __init__(self, parent=None, position=None):
        self.g_pos, self.h_pos, self.f_pos = 0, 0, 0
        self.parent = parent
        self.position = position

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return str(self.position)


def get_result_path(square):
    path = []
    current = square
    while current is not None:
        path.append(current.position)
        current = current.parent
    return list(reversed(path))


def is_square_in_board(position):
    return position[0] >= BOARD_SIZE[0] or position[0] < 0 or position[1] >= BOARD_SIZE[1] or position[1] < 0


def is_square_a_wall(board, position):
    return board[position[0]][position[1]] == 5


def a_star(board):
    start = [0, 0]
    end = [19, 19]
    end_square = Square(position=end)
    list_open = [Square(position=start)]
    list_closed = []

    while len(list_open) > 0:
        current_square = list_open[0]
        current_index = 0
        for index, square in enumerate(list_open):
            if square.f_pos <= current_square.f_pos:
                current_square = square
                current_index = index

        list_open.pop(current_index)
        list_closed.append(current_square)

        if current_square == end_square:
            return get_result_path(current_square)
        children = []
        for new_position in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            square_pos = [current_square.position[0] + new_position[0], current_square.position[1] + new_position[1]]

            if is_square_in_board(square_pos) or is_square_a_wall(board, square_pos):
                continue

            children.append(Square(current_square, square_pos))

        for child in children:
            if child in list_closed:
                continue

            child.g_pos = current_square.g_pos + 1
            child.h_pos = sqrt(((child.position[0] - end_square.position[0]) ** 2) + ((child.position[1] - end_square.position[1]) ** 2))
            child.f_pos = child.g_pos + child.h_pos

            if len([i for i in list_open if child == i and child.g_pos >= i.g_pos]) > 0:
                continue

            list_open.append(child)


board = [[0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
         [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
         [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 5, 0, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 5, 5, 0, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 5, 5, 0, 5, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 5, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [5, 5, 5, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


if __name__ == '__main__':
    BOARD_SIZE = [len(board), len(board[0])]
    print(a_star(board))