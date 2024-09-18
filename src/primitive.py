from sympy import isprime, primerange


def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1  # equivalently, y = y // 2
        x = (x * x) % p
    return res


def find_primitive(n):
    if not isprime(n):
        return "The input has to be a prime number."

    phi = n - 1  # Euler Totient Function for prime number is n-1
    # print('phi = ', phi)
    prime_factors = list(primerange(1, phi + 1))
    # print('prime_factors = ', prime_factors)
    for g in range(2, n + 1):
        # print(g)
        flag = False
        for factor in prime_factors:
            if power(g, phi // factor, n) == 1:
                flag = True
        if not flag:
            return g  # If no break occurs in the loop, this is a primitive root modulo n
    return -1


if __name__ == '__main__':
    print('primitive of 7 = ', find_primitive(7))
    print('primitive of 11 = ', find_primitive(11))
    print('primitive of 7340033 = ', find_primitive(7340033))
