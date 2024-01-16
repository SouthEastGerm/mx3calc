def determinant_a(e, f, h, i):
    return 1 * (e * i - f * h)

def determinant_b(d, f, g, i):
    return -1 * (d * i - f * g)

def determinant_c(d, e, g, h):
    return 1 * (d * h - e * g)

def determinant_d(b, c, h, i):
    return -1 * (b * i - c * h)

def determinant_e(a, c, g, i):
    return 1 * (a * i - c * g)

def determinant_f(a, b, g, h):
    return -1 * (a * h - b * g)

def determinant_g(b, c, e, f):
    return 1 * (b * f - c * e)

def determinant_h(a, c, d, f):
    return -1 * (a * f - c * d)

def determinant_i(a, b, d, e):
    return 1 * (a * e - b * d)

def main():
    # Input the 3x3 matrix
    a, b, c = map(int, input("Enter values for the first row (a b c): ").split())
    d, e, f = map(int, input("Enter values for the second row (d e f): ").split())
    g, h, i = map(int, input("Enter values for the third row (g h i): ").split())

    # Calculate determinants for each cell
    determinant_a_value = determinant_a(e, f, h, i)
    determinant_b_value = determinant_b(d, f, g, i)
    determinant_c_value = determinant_c(d, e, g, h)
    determinant_d_value = determinant_d(b, c, h, i)
    determinant_e_value = determinant_e(a, c, g, i)
    determinant_f_value = determinant_f(a, b, g, h)
    determinant_g_value = determinant_g(b, c, e, f)
    determinant_h_value = determinant_h(a, c, d, f)
    determinant_i_value = determinant_i(a, b, d, e)

    # Calculate the transpose of the matrix of cofactors
    cofactor_matrix_transpose = [
        [determinant_a_value, determinant_b_value, determinant_c_value],
        [determinant_d_value, determinant_e_value, determinant_f_value],
        [determinant_g_value, determinant_h_value, determinant_i_value]
    ]

    # Inverse of (A)
    inverse = [
        [determinant_a_value, determinant_d_value, determinant_g_value],
        [determinant_b_value, determinant_e_value, determinant_h_value],
        [determinant_c_value, determinant_f_value, determinant_i_value]
    ]
    # Display adj(A) and Inverted(A)
    print("adj(A) =")
    for row in cofactor_matrix_transpose:
        print(row)

    # Calculate the determinant of the original matrix
    determinant_original_matrix = a * determinant_a_value + b * determinant_b_value + c * determinant_c_value
    if determinant_original_matrix == 0:
        print("Inverted(A) is undefined as the determinant of the original matrix is zero.")
    else:
        print("\nInverted(A) =")
        for row in inverse:
            print(row)

        # Input the system of linear equations
        x, y, z = map(float, input("\nEnter the system of linear equations (x, y, z): ").split())

        # Display the new 3x3 matrix
        new_matrix = [
            [determinant_a_value * x, determinant_d_value * y, determinant_g_value * z],
            [determinant_b_value * x, determinant_e_value * y, determinant_h_value * z],
            [determinant_c_value * x, determinant_f_value * y, determinant_i_value * z]
        ]
        print("\nNew 3x3 matrix:")
        for row in new_matrix:
            print(row)

        # Proof of inversion
        print("\nProof of inversion = ")
        for row in new_matrix:
            print(sum(row))

if __name__ == "__main__":
    main()