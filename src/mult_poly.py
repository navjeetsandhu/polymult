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

def mult_poly_naive_q(p1, p2, q):
    # schoolbook multiplication
    tmp = mult_poly_naive(p1, p2)

    # wrap around q
    for i in range(len(tmp)):
        tmp[i] = (tmp[i]) % q

    return tmp


# Cyclic Convolution (CC)
# The degree of the polynomial will only grow larger
# and larger as we perform more multiplications. That means we need to have longer
# arrays to store coefficients and more complex convolutions every time a
# multiplication is performed.  It would be great if the degree of the polynomials
# could wrap around just like the coefficients.
# we can take modulo some polynomial ϕ(x) after every polynomial operation.
# The resulting polynomial’s degree would never be larger or equal to the degree of ϕ(x).
# We call such structure Zq[x]/(ϕ(x)
# when ϕ(x)=xd−1. If we take any polynomial modulo xd−1, it’s equivalent to removing
# multiples of xd−1 from the polynomial until the resulting polynomial has degree lower than d

def mult_poly_naive_q_cc(p1, p2, q, d):
    tmp = mult_poly_naive_q(p1, p2, q)

    # take polynomial modulo x^d - 1
    for i in range(d, len(tmp)):
        tmp[i - d] = (tmp[i - d] + tmp[i]) % q
        tmp[i] = 0

    return tmp[:d]

# Negative wrapped convolution (negacyclic convolution)
# modulus ϕ(x)=xd+1 
def mult_poly_naive_q_nwc(p1, p2, q, d):
    tmp = mult_poly_naive_q(p1, p2, q)

    # take polynomial modulo x^d - 1
    for i in range(d, len(tmp)):
        tmp[i - d] = (tmp[i - d] - tmp[i]) % q
        tmp[i] = 0

    return tmp[:d]


def test_mult_poly():
    a = [1, 2, 3, 4]
    b = [1, 3, 5, 7]
    print("Schoolbook Multiplication: ")
    print(mult_poly_naive(a, b))
    # [1, 5, 14, 30, 41, 41, 28]
    print("Integers modulo a prime number q: q = 17")
    print(mult_poly_naive_q(a, b, 17))
    # [1, 5, 14, 13, 7, 7, 11]
    print("Cyclic Convolution (CC): q = 17 d =4 ")
    print(mult_poly_naive_q_cc(a, b, 17, 4))
    # [8, 12, 8, 13]
    print("Negative wrapped convolution (negacyclic convolution): q = 17 d =4 ")
    print(mult_poly_naive_q_nwc(a, b, 17, 4))
    # [11, 15, 3, 13]


if __name__ == '__main__':
    test_mult_poly()
