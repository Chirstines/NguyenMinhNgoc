# greatest common divisor with Euclid algorithm
def GCD(a, b):
    if (b == 0):
        return a
    return GCD(b, a % b)

def probability_of_coprime(n = 1000):
    cnt = 0
    for i in range (n - 1):
        for j in range (i + 1, n):
            if i != j and GCD(i, j) == 1:
                cnt += 1
    return cnt / (n * (n - 1) / 2)
print(probability_of_coprime())
