def matrix_print(cicle_count: int):
    print('\n'.join([' '.join(['1' if i == j else '0' for j in range(cicle_count)]) for i in range(cicle_count)]))

def get_matrix_size() -> str:
    pass


def main():
    matrix_size = int(input("Введите размер матрицы: "))
    matrix_print(matrix_size)

if __name__ == "__main__":
    main()
