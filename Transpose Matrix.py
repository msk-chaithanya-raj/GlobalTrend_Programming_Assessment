def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]
def transpose_matrix_operations():
    matrix = []
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} values (space-separated): ").split()))
        matrix.append(row)
    transposed = transpose_matrix(matrix)
    print("Transposed Matrix:")
    for row in transposed:
        print(row)
transpose_matrix_operations()
