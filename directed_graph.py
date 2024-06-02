import turtle

from constants import SEED, NUM_VERTICES, K
from matrix_utils import (print_matrix, create_directed_matrix)
from graph import draw_graph


def main():
    directed_matrix = create_directed_matrix(SEED, NUM_VERTICES, K)
    print('Directed matrix:')
    print_matrix(directed_matrix)
    draw_graph(directed_matrix, True)



    turtle.exitonclick()


if __name__ == '__main__':
    main()
