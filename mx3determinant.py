def determinant_a(e, f, h, i):
    return 1*(e * i - f * h)

def determinant_b(d, f, g, i):
    return -1*(d * i - f * g)

def determinant_c(d, e, g, h):
    return 1*(d * h - e * g)

def determinant_d(b, c, h, i):
    return -1*(b * i - c * h)

def determinant_e(a, c, g, i):
    return 1*(a * i - c * g)

def determinant_f(a, b, g, h):
    return -1*(a * h - b * g)

def determinant_g(b, c, e, f):
    return 1*(b * f - c * e)

def determinant_h(a, c, d, f):
    return -1*(a * f - c * d)

def determinant_i(a, b, d, e):
    return 1*(a * e - b * d)

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

    # Display results
    print("Determinant for a:", determinant_a_value)
    print("Determinant for b:", determinant_b_value)
    print("Determinant for c:", determinant_c_value)
    print("Determinant for d:", determinant_d_value)
    print("Determinant for e:", determinant_e_value)
    print("Determinant for f:", determinant_f_value)
    print("Determinant for g:", determinant_g_value)
    print("Determinant for h:", determinant_h_value)
    print("Determinant for i:", determinant_i_value)

if __name__ == "__main__":
    main()
