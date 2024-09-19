"""
Simple code for polynomial multiplication.
The code assumes the two inputs have the same order, does not consider edge cases
and does not perform any check on the inputs.
"""

import numpy as np


def polynomial_multiply(A, B):
    # Schoolbook multiplication of two polynomials A and B
    n = len(A) - 1
    result = [0] * (2 * n + 1)
    # Multiply each term of A with each term of B and accumulate the result
    for i in range(n + 1):
        for j in range(n + 1):
            result[i + j] += A[i] * B[j]
    return result


def polynomial_multiply_fft(A, B):
    # Multiplication of two polynomials A and B using FFT
    n = len(A) + len(B) - 1
    next_power_of_2 = 2 ** (n - 1).bit_length()
    # Pad the input polynomials with zeros until their length is a power of 2
    a_padded = np.pad(A, (0, next_power_of_2 - len(A)), mode='constant')
    b_padded = np.pad(B, (0, next_power_of_2 - len(B)), mode='constant')
    # Compute the FFT of the input polynomials
    a_fft = np.fft.fft(a_padded)
    b_fft = np.fft.fft(b_padded)
    # Multiply the transformed polynomials element-wise
    result_fft = a_fft * b_fft
    # Compute the inverse FFT of the result to obtain the coefficients of the product
    # polynomial
    result = np.fft.ifft(result_fft).real.round()
    result = result[:n]
    return result


def polynomial_multiply_ntt(A, B):
    # Multiplication of two polynomials A and B using NTT
    # p is the modulous: a prime number such that p = k * 2ˆn + 1 for some integer k
    # g is a primitive root modulo p
    p, g = 7340033, 3
    n = max(len(A), len(B))
    n = 1 << (n - 1).bit_length()
    # Pad the input polynomials with zeros until their length is a power of 2
    A += [0] * (n - len(A))
    B += [0] * (n - len(B))
    w = pow(g, (p - 1) // n, p)
    # Precompute bit-reversed indices
    rev = [0] * n
    for i in range(n):
        rev[i] = rev[i >> 1] >> 1 | (i & 1) * (n >> 1)

    def ntt(f, inv=False):
        # Compute the NTT or inverse NTT of a polynomial f using an iterative CooleyTukey FFT algorithm
        for i in range(n):
            if i < rev[i]:
                f[i], f[rev[i]] = f[rev[i]], f[i]
        k = 2
        while k <= n:
            wn = pow(w, n // k, p)
            if inv:
                wn = pow(wn, p - 2, p)
            for i in range(0, n, k):
                w_ = 1
                for j in range(k // 2):
                    x, y = f[i + j], f[i + j + k // 2] * w_ % p
                    f[i + j], f[i + j + k // 2] = (x + y) % p, (x - y) % p
                    w_ = w_ * wn % p
            k <<= 1
        if inv:
            inv_n = pow(n, p - 2, p)
            for i in range(n):
                f[i] = f[i] * inv_n % p

    C = [0] * n
    # Compute the NTT of the input polynomials and multiply them element-wise
    ntt(A), ntt(B)
    for i in range(n):
        C[i] = A[i] * B[i] % p
    # Compute the inverse NTT of the result to obtain the coefficients of the product
    # polynomial
    ntt(C, True)
    # Reduce the coefficients modulo p to bring them into the desired range
    # [-p//2, p//2]
    for i in range(n):
        if C[i] > (p - 1) // 2:
            C[i] -= p
    return C


def test_one():
    # Example usage
    a = [1, 2, 3]  # Coefficients of a(x) = xˆ2 + 2x + 3
    b = [2, -1, 0]  # Coefficients of B(x) = 2x - xˆ0
    print('Result of Schoolbook Multiplication:', polynomial_multiply(a, b))
    print('Result of Multiplication using FFT:', polynomial_multiply_fft(a, b))
    print('Result of Multiplication using NTT:', polynomial_multiply_ntt(a, b))


# Result of Schoolbook Multiplication: [2, 3, 4, -3, 0]
# Result of Multiplication using FFT: [ 2.  3.  4. -3.  0.]
# Result of Multiplication using NTT: [2, 3, 4, -3]


def test_two():
    # Example usage
    a = [1, 2, 3]
    b = [1, 2, 3]
    print('Result of Schoolbook Multiplication:', polynomial_multiply(a, b))
    print('Result of Multiplication using FFT:', polynomial_multiply_fft(a, b))
    print('Result of Multiplication using NTT:', polynomial_multiply_ntt(a, b))


def test_three():
    # Example usage
    a = [1, 2, 3, 4]
    b = [1, 2, 3, 4]
    print('Result of Schoolbook Multiplication:', polynomial_multiply(a, b))
    print('Result of Multiplication using FFT:', polynomial_multiply_fft(a, b))
    print('Result of Multiplication using NTT:', polynomial_multiply_ntt(a, b))


if __name__ == '__main__':
    test_three()
