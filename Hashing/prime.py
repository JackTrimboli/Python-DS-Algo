'''
Get all prime numbers in an array
'''


def getNumPrimes(num):
    primes = []

    # for each value from the start of the array to the stopping point,
    for i in range(2, num+1):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:  # if i divides evenly into j and is not equal to j
                break
        else:
            primes.append(i)
    return len(primes)


print(getNumPrimes(1000000000))
