# Напишите функцию для транспонирования матрицы

MATRIX = [
    [1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4],
]

def main():
    print("Исходная матрица:")
    print_matrix(MATRIX)
    print("Транспонированная:")
    print_matrix(transpose_matrix(MATRIX))

def print_matrix(matrix: list[list]):
    # Вывод квадратной матрицы на экран
    for row in matrix:
        print(row)

def transpose_matrix(matrix: list[list]) -> list[list]:
    # Транспонирование матрицы
    new_matrix = [[] for _ in range(0, len(matrix[0]))]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            new_matrix[col].append(matrix[row][col])
    return new_matrix

if __name__ == "__main__":
    main()




# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

GLOBAL_VALUE = 23

def my_func(**kwargs) -> dict:
    # Функция подготовки словаря из переданных аргументов и их значений
    result = dict()
    for k, v in kwargs.items():
        try:
            _ = hash(v)
            result[v] = k
        except TypeError:
            result[str(v)] = k

    return result

def main():
    print("Исх. параметры: first=\"one\", second=2, third=3, fourth=\"four\", fifth=[2, 3]")
    print(my_func(first="one", second=2, third=3, fourth="four", fifth=[2, 3]))

if __name__ == "__main__":
    main()






