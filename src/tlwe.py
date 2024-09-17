# This code is just for illustration purposes. It does not work in $\mathbb{Z}/q\mathbb
# {Z}$, instead it uses np.float64, and is not efficient.

import numpy as np

# Function to perform modular arithmetic on the Torus
def mod_torus(x):
    return x - np.floor(x + 0.5)

# Function to perform dot product modulo the Torus
def dot_torus(a, b):
    return mod_torus(np.dot(a, b))

# Parameters
n = 6 #Dimension of the TLWE vectors
sigma = 0.01 #The standard deviation of the error term

#Key Generation and preparing a trivial TLWE sample
sk = np.random.randint(0, 2, n) #Secret key: binary vector of n bits.
print("sk=", sk)

a = np.random.uniform(-0.5, 0.5, n) #Random vector of n real values in the Torus
print("a=", a)

e = mod_torus(np.random.normal(0, sigma)) #Random error term in the Torus
print("e=", e)

b = mod_torus(dot_torus(a, sk) + e) #Encrypted value in the Torus
print("b=", b)

# Message and Encryption
m = np.random.randint(0, 2) #Random binary message
print("m=", m)

m_b = mod_torus(m * 0.5 - 0.25) #Convert message to the Torus
print("m_b=", m_b)

c_a = a #First part of ciphertext remains the same
print("c_a=", c_a)

c_b = mod_torus(b + m_b) #Second part of ciphertext with message
print("c_b=", c_b)

c = np.append(c_a, c_b) #Complete ciphertext
print("c=", c)

# Decryption
c_a = c[:-1] # Extract first part of ciphertext
print("c_a=", c_a)

c_b = c[-1] # Extract second part of ciphertext
print("c_b=", c_b)

phi = mod_torus(c_b - dot_torus(c_a, sk)) # Compute phase difference
print("phi", phi)

d = int(round(phi * 2 + 0.5)) % 2 # Decrypted message
print("d=", d)

print("The input message m =", m, "and the decryption is d=", d)
assert m == d, "Input message and decryption are not equal"
