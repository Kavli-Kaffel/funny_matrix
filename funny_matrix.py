# def matrix_print(cicle_count: int):
#     # print('\n'.join([' '.join(['1' if i == j else '0' for j in range(cicle_count)]) for i in range(cicle_count)]))
#     # step_nun номер шага
#     # line_nun номер строки
#     # el_num номер элемента

#     for step_nun in range(cicle_count):
#         for line_nun in range(cicle_count):
#             for el_num in range(cicle_count):
#                 if line_nun % 2 == 0:
#                     if line_nun + step_nun == el_num:
#                         print("1", end="")
#                     else:
#                         print("0", end="")
#                 else:
#                     if line_nun - step_nun == el_num:
#                         print("1", end="")
#                     else:
#                         print("0", end="")
#             print("")
#         print("\n")

import time


def get_matrix_size() -> int:
    return int(input("Введите размер матрицы: "))


def generate_ones(matrix_size: int):  # -> list[tuple[int, int]]:
    """
    Генерация единиц в виде массива координат в матрице
    Генерация представления матрицы в виде массива координат единиц
    Пример
    [(0,0),(1,1),...(n,n)]
    """
    matrix = [(0, 0)]
    for i in range(1, matrix_size):
        matrix = matrix + [(i, i)]
    # return [(0, 0), (1, 1), (2, 2)]
    return matrix


def transform_matrix(matrix: list[tuple[int, int]]):
    # for i in range(len(matrix)):
    # my_list[1] = (7, 7)
    pass


def print_matrix(matrix: list[tuple[int, int]]):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i, j) == matrix[i]:
                print("1", end="")
            else:
                print("0", end="")
        print("")
    print("")


def main():
    matrix_size = get_matrix_size()
    # Matrix = [[0 for x in range(matrix_size)] for y in range(matrix_size)]
    # matrix_print(matrix_size)
    matrix = generate_ones(matrix_size)
    while True:
        print_matrix(matrix)
        # print(matrix_size)
        time.sleep(1)


if __name__ == "__main__":
    main()
