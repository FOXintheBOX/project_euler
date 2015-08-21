def is_prime(x):
    if x == 0 or x == 1:
        return True
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def prime_factors(target):
    primes=[]
    i = 2
    while i < target**0.5:
        if is_prime(i) and target % i == 0:
            primes.append(i)
            target /= i
            print "prime found: " + str(i)
            i = 2
        i += 1
    primes.append(target)
    return primes

print prime_factors(600851475143)
