def horners_method(coeffs, x, k=0):
    """
    Evaluate horners_method for a polynomial with coefficients 'coeffs'
    for the value x, starting at position k.
    """
    if k == len(coeffs) - 1:
        return coeffs[k]
    else:
        return coeffs[k] + x * horners_method(coeffs, x, k + 1)


def to_point_value(coeffs, x_pts):
    result = []
    for k in range(0, len(coeffs)):
        result.append((x_pts[k], horners_method(coeffs, x_pts[k])))
    return result


def test_one():
    # Example usage
    C_e = [1, 2, 3]
    C_a = [4, -3, 2, -4]
    C_b = [1, 7, 2, 3]
    X = [4, 5, 6]

    X1 = [4, 3, 9, -3]

    C_c = [C_a[i] + C_b[i] for i in range(0, len(C_a))]

    A = to_point_value(C_a, X1)
    B = to_point_value(C_b, X1)
    C = to_point_value(C_c, X1)

    print("A", A)
    print("B", B)
    print("C", C)


if __name__ == '__main__':
    test_one()
