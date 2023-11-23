import time


def get_matrix_size() -> int:
    return int(input("Введите размер матрицы: "))


def generate_ones(matrix_size: int) -> list[tuple[int, int]]:
    """
    Генерация единиц в виде массива координат в матрице
    Генерация представления матрицы в виде массива координат единиц
    Пример
    [(0,0),(1,1),...(n,n)]
    """
    return [(i, i) for i in range(matrix_size)]


def transform_matrix(matrix: list[tuple[int, int]]):
    j = 0
    for i in range(len(matrix)):
        if matrix[i][1] < len(matrix) - j - 1 and matrix[i][0] == j:
            matrix[i] = (matrix[i][0], matrix[i][1] + 1)
        elif matrix[i][1] == len(matrix) - j - 1 and matrix[i][0] < len(matrix) - j - 1:
            matrix[i] = (matrix[i][0] + 1, matrix[i][1])
        elif matrix[i][0] == len(matrix) - j - 1 and matrix[i][1] > j:
            matrix[i] = (matrix[i][0], matrix[i][1] - 1)
        elif matrix[i][1] == j and matrix[i][0] > j:
            matrix[i] = (matrix[i][0] - 1, matrix[i][1])

        if (i < (len(matrix)) // 2 and len(matrix) % 2 != 0) or (i < (len(matrix) - 1) // 2 and len(matrix) % 2 == 0):
            j += 1
        elif (i >= (len(matrix)) // 2 and len(matrix) % 2 != 0) or (i >= (len(matrix)) // 2 and len(matrix) % 2 == 0):
            j -= 1
    return matrix


def print_matrix(matrix: list[tuple[int, int]]):
    set_matrix = set(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i, j) in set_matrix:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print("")
    print("")
    # TODO Стирать и печатать


def main():
    matrix_size = get_matrix_size()
    matrix = generate_ones(matrix_size)
    while True:
        print_matrix(matrix)
        matrix = transform_matrix(matrix)
        time.sleep(1)

if __name__ == "__main__":
    main()
