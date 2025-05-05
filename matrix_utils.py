# matrix_utils.py

def get_matrix_minor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]

def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Determinant is only defined for square matrices.")

    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    det = 0
    for c in range(len(matrix)):
        det += ((-1)**c) * matrix[0][c] * determinant(get_matrix_minor(matrix, 0, c))
    return det

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]

def inverse(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Only square matrices can be inverted.")

    det = determinant(matrix)
    if det == 0:
        raise ValueError("Matrix is singular and cannot be inverted.")

    if len(matrix) == 2:
        return [[matrix[1][1]/det, -matrix[0][1]/det],
                [-matrix[1][0]/det, matrix[0][0]/det]]

    cofactors = []
    for r in range(len(matrix)):
        cofactor_row = []
        for c in range(len(matrix)):
            minor = get_matrix_minor(matrix, r, c)
            cofactor = ((-1)**(r+c)) * determinant(minor)
            cofactor_row.append(cofactor)
        cofactors.append(cofactor_row)

    adjugate = transpose(cofactors)
    return [[elem / det for elem in row] for row in adjugate]

# Optional: test the module
if __name__ == "__main__":
    sample_matrix = [
        [4, 7],
        [2, 6]
    ]
    print("Original Matrix:")
    for row in sample_matrix:
        print(row)

    try:
        inv = inverse(sample_matrix)
        print("\nInverse Matrix:")
        for row in inv:
            print(row)
    except ValueError as e:
        print("Error:", e)
