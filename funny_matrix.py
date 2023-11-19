def matrix_print(cicle_count: int):
    #print('\n'.join([' '.join(['1' if i == j else '0' for j in range(cicle_count)]) for i in range(cicle_count)]))
    #step_nun номер шага
    #line_nun номер строки
    #el_num номер элемента

    for step_nun in range (cicle_count):
        for line_nun in range (cicle_count):
            for el_num in range(cicle_count):
                if line_nun % 2 == 0:
                    if line_nun+step_nun == el_num:
                        print('1', end='')
                    else:
                        print('0', end='') 
                else:
                    if line_nun-step_nun == el_num:
                        print('1', end='')
                    else: 
                        print('0', end='') 
            print('')
        print('\n')

def get_matrix_size() -> str:
    pass


def main():
    matrix_size = int(input("Введите размер матрицы: "))
    matrix_print(matrix_size)

if __name__ == "__main__":
    main()
