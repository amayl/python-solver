# number of unknown variables
n = int(input("Enter number of unknowns: "))

m1 = [] # main list
def enter_matrix(n): # ts always gonna be a square matrix, cuz you can only inverse sqaure matrices
    for i in range(n):
        l = [] # local list
        for j in range(n):
            v = int(input(f"Enter value {i+1},{j+1}: "))
            l.append(v)
        m1.append(l)
    return m1

m2 = []
def enter_vector(n):
    for i in range(n):
        l = [] # local list
        for j in range(1):
            v = int(input(f"Enter value {i+1}: "))
            l.append(v)
        m2.append(l)
    return m2

new_matrix = enter_matrix(n)

from matrix_utils import inverse

inverse_matrix = inverse(new_matrix)
answer_vector = enter_vector(n)

def multiply_matrix(inverse_matrix, answer_vector):
    A = inverse_matrix
    B = answer_vector
    result = []
    for i in range(len(A)):  # Rows of A
        row = []
        for j in range(len(B[0])):  # Columns of B
            total = 0
            for k in range(len(B)):  # Rows of B or Columns of A
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)

    return result

answer = multiply_matrix(inverse_matrix, answer_vector)

print(new_matrix)
print(answer_vector)
print(inverse_matrix)
print(f"The answer is \n{answer}")

