primes = [True] * 1000

primes[0] = False
primes[1] = False

for index in range(2, 32):
    if primes[index]:

        for prime in range(index * 2, 1000, index):
            primes[prime] = False

for index in range(1000):
    if primes[index]:
        print(index)
