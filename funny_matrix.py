def greeting(name: str):
    print(f"Hello {name}!")


def get_matrix_size() -> str:
    return input("Введите размер матрицы:")


def main():
    matrix_size = get_matrix_size()
    greeting(matrix_size)


if __name__ == "__main__":
    main()