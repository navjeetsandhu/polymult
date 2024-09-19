# https://cryptographycaffe.sandboxaq.com/posts/ntt-01/
# Adding two polynomials is as simple as just summing up their coefficients.
# Multiplying a polynomial by a constant is just multiplying every coefficient by that constant.
# However, when we want to multiply polynomials, things get slightly more complicated.

def mult_poly_naive(p1, p2):
    result = [0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] += p1[i] * p2[j]
    return result


def test_mult_poly_naive():
    a = [1, 2, 3, 4]
    b = [1, 3, 5, 7]
    print(mult_poly_naive(a, b))
    # [1, 5, 14, 30, 41, 41, 28]





if __name__ == '__main__':
    test_mult_poly_naive()