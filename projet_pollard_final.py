## création de fonctions de bases :
## 1. isprime(n) : vérifie si un nombre est premier



def is_prime(n):
    if n < 2 or n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**(1/2))+1,2):
            if (n % i) == 0:
                return False
    return True

## 2. gcd(a,b) : calcule le pgcd de deux nombres
def pgcd(a, b):
    """
    input: a and b two integers
    return: (g, x, y) three integers such that a*x + b*y = g = gcd(a, b)
    """
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    tu = (b, x0, y0)
    return tu[0]


## modexp : calcule a^i mod n
def modexp(a, i, n):
    result = 1
    a = a % n  # Réduire a si nécessaire
    while i > 0:
        if i % 2 == 1:
            result = (result * a) % n
        i = i >> 1
        a = (a * a) % n
    return result



def pollard(n, iterations = 1):
    a = 2
    i = 2
    factor = []
    while n % 2 == 0:
        factor.append(2)
        n //= 2
    while n != 1:
        print("Factoring ", n)
        if is_prime(n):
            print(n, "is already a prime, thus it is a factor")
            factor.append(n)
            factor.sort()
            return factor
        a_old = a
        a = modexp(a, i, n)
        print("a =", a_old, "^", i, "mod", n, "=", a)
        d = pgcd(a - 1, n)
        n_old = n
        if 1 < d and d < n:
            factor.append(d)
            n //= d
            i = 1
        if d == 1:
            print("d = gcd(", a, "- 1,", n_old, ") =", d)
        else:
            print("d = gcd(", a, "- 1,", n_old, ") =", d, "is a factor")
            print("Now, factoring ", n_old, "/", d, "=", n_old / d)
            print()
        iterations += 1
        i += 1
    return factor
 

# Test de la fonction
number = 123469
factors = pollard(number)
print("Factors of", number, ":", factors)

