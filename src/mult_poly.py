
# https://cryptographycaffe.sandboxaq.com/posts/ntt-01/


# Schoolbook Multiplication
# Adding two polynomials is as simple as just summing up their coefficients.
# Multiplying a polynomial by a constant is just multiplying every coefficient by that constant.
# However, when we want to multiply polynomials, things get slightly more complicated.

def mult_poly_naive(p1, p2):
    result = [0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] += p1[i] * p2[j]
    return result



# integers modulo a prime number q
# The interesting thing about working in a finite field is that the polynomial coefficients
# “wrap around” when being multiplied. So regardless of how much polynomial arithmetic we
# perform, the coefficients of the polynomial can still be bounded in a fixed range

def mul_poly_naive_q(a, b, q):
    tmp = [0] * (len(a) + len(b) - 1)  # the product of two polynomials cannot exceed the sum of their degree

    # schoolbook multiplication
    for i in range(len(a)):
        # perform a_i * b
        for j in range(len(b)):
            tmp[i + j] = (tmp[i + j] + a[i] * b[j]) % q

    return tmp


def test_mult_poly():
    a = [1, 2, 3, 4]
    b = [1, 3, 5, 7]
    print ("Schoolbook Multiplication: ")
    print(mult_poly_naive(a, b))
    # [1, 5, 14, 30, 41, 41, 28]
    print("Integers modulo a prime number q: ")
    print(mul_poly_naive_q(a, b, 17))

if __name__ == '__main__':
    test_mult_poly()