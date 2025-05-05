# number of unknown variables
n = int(input("Enter number of unknowns: "))

m = [] # main list
def enter_matrix(): # ts always gonna be a square matrix, cuz you can only inverse sqaure matrices
    for i in range(n):
        l = [] # local list
        for j in range(n):
            v = int(input(f"Enter value {i+1},{j+1}: "))
            l.append(v)
        m.append(l)
    return m

print(enter_matrix())