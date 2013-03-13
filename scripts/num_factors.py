
import sys
from collections import Counter
import multiprocessing
from IPython.parallel import Client

def factorize(n):
    if n < 2:
        return []
    factors = []
    p = 2

    while True:
        if n == 1:
            return factors
        r = n % p
        if r == 0:
            factors.append(p)
            n = n / p
        elif p * p >= n:
            factors.append(n)
            return factors
        elif p > 2:
            p += 2
        else:
            p += 1

def serial_factorization(low_limit, high_limit):
    num_factors = []
    for i in range(low_limit, high_limit):
        num_factors.append(len(Counter(factorize(i))))
    num_uniq = Counter(num_factors)
    return num_uniq

def multi_factorization(low_limit, high_limit):
    pool = multiprocessing.Pool(processes=4)
    factor_map = pool.map(factorize, range(low_limit, high_limit))
    num_factors = []
    for i in factor_map:
        num_factors.append(len(Counter(i)))
    num_uniq = Counter(num_factors)
    return num_uniq

def ipython_factorization(low_limit, high_limit):
    try:
        client = Client()
        direct_view = client[:]

        @direct_view.parallel(block=True)
        def factorize(n):
            if n < 2:
                return []
            factors = []
            p = 2
        
            while True:
                if n == 1:
                    return factors
                r = n % p
                if r == 0:
                    factors.append(p)
                    n = n / p
                elif p * p >= n:
                    factors.append(n)
                    return factors
                elif p > 2:
                    p += 2
                else:
                    p += 1

        num_factors = []
        factor_map = factorize.map(range(low_limit, high_limit))
        for i in factor_map:
            num_factors.append(len(Counter(i)))
        num_uniq = Counter(num_factors)
        return num_uniq
    except IOError:
        sys.exit("IOError: Make sure to run 'ipcluster start -n 4' first")

def main():
    low_limit = 2
    high_limit = 500001
    if sys.argv[1] == 's':
        counts = serial_factorization(low_limit, high_limit)
    if sys.argv[1] == 'm':
        counts = multi_factorization(low_limit, high_limit)
    if sys.argv[1] == 'i':
        counts = ipython_factorization(low_limit, high_limit)
    
    print dict(counts)

if __name__ == '__main__':
    main()